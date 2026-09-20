# SICP 服务器部署

- 域名：`sicp.zzzping.top`
- 服务器：`39.106.147.77`，Ubuntu 22.04、Nginx 1.18
- 页面版本：`94f9b9fe5f444c0e519d74cee368a264c65d53df`
- 发布目录：`/var/www/sicp.zzzping.top/releases/20260920-94f9b9f`
- 当前版本软链接：`/var/www/sicp.zzzping.top/current`
- Nginx 文档根目录：`/var/www/sicp.zzzping.top/current/html`
- Nginx 站点配置：`/etc/nginx/sites-available/sicp.zzzping.top`
- 日志：`/var/log/nginx/sicp.zzzping.top.access.log` 和同目录下的 `sicp.zzzping.top.error.log`

当前状态：2026-09-20 已部署并启用 HTTPS。访问 `https://sicp.zzzping.top/` 默认进入中文版。Chrome 公网访问、顶部语言切换和首页底部导航已经验证。`nginx-sicp.conf` 与服务器启用的站点配置一致。

## 发布内容

部署包从 Git 提交生成，只包含 `html` 和 `LICENSE`。不上传仓库历史、翻译脚本、翻译缓存、密钥和其他本地未跟踪文件。保留 `html` 目录层级，避免把仓库根目录的封面 `index.xhtml` 覆盖到正文目录首页上。

```powershell
git archive --format=tar.gz --output=sicp-release.tar.gz HEAD html LICENSE
```

上传后解压到新的 `releases/<版本>` 目录，检查页面，再原子替换 `current` 软链接。保留旧发布目录以便回滚。静态文件更新不需要重启 Nginx；配置变更先运行 `nginx -t`，通过后再 `systemctl reload nginx`。

站点根路径跳转到 `/index_zh.xhtml`，英文首页为 `/index.xhtml`。服务器沿用全局 MIME 配置，将 `.xhtml` 返回为 `application/xhtml+xml`，JavaScript 返回为 `application/javascript`。浏览器缓存需要重新验证，避免旧脚本造成阅读控件缺失。

## HTTPS 与域名验证

现有项目使用 Certbot / Let's Encrypt，本项目使用独立证书。TLS 参数复用服务器现有的 `/etc/letsencrypt/options-ssl-nginx.conf` 和 `ssl-dhparams.pem`，不修改其他站点配置或证书。

2026-09-20 的公网检查中，HTTP 请求被阿里云返回的 `Non-compliance ICP Filing` 页面拦截，HTTP-01 验证失败。因此本次改用手动 DNS-01 验证，证书已成功签发，过期时间为 **2026-12-19 12:53:51 UTC（北京时间 20:53:51）**。

公网 Chrome 已确认 HTTPS 页面可以访问；普通 HTTP 仍返回阿里云拦截页，用户需直接使用完整的 `https://` 地址。服务器中的 HTTP 到 HTTPS 跳转配置已就绪，但不能保证云平台拦截前的请求会到达 Nginx。另一本机 Windows curl 客户端的 HTTPS 连接被重置，因此不能据此保证所有网络和客户端的可达性。

手动 DNS 验证签发的证书需要再次完成 DNS 验证才能续期。服务器已有 `certbot.timer`，但它无法自动完成手动 TXT 验证。若要自动续期，需要另行配置 DNS 服务商 API 的认证钩子及最小权限凭据；不得把凭据提交到仓库。

申请或续期命令：

```bash
certbot certonly --manual --preferred-challenges dns \
  --cert-name sicp.zzzping.top -d sicp.zzzping.top
```

按照 Certbot 输出添加 `_acme-challenge.sicp` 的 TXT 记录，确认 DNS 已生效后继续。证书签发成功后运行 `nginx -t && systemctl reload nginx`，并检查证书有效期和页面访问。
