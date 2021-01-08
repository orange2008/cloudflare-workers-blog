# Tutorials

## Tools & Materials

A cloudflare account.

Internet connection*

## Tutorial

1. Register a Cloudflare account, which you should already did that.
2. Go to [Cloudflare Dashboard](https://dash.cloudflare.com)
3. Click 'Workers' and choose the free plan.
4. Create a Worker. Enter whatever domain you want.![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108192837.png)

![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108193006.png)

5. Copy `index.js`'s all text to the Script box.
6. Change some values.(_cfblog.orwtmc.top_ is my domain, don't use it!)![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108193625.png)

### Get zone ID.

1. You may need to buy a domain and transfer it to Cloudflare, if you don't have money, please use freenom.
2. After you done that, please go to your domain's dashboard and copy the Zone ID.(Click it in Cloudflare dashboard.)![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108193926.png)

3. Copy this zone ID and paste it to the previous page's another blank.![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108194120.png)

### Get API Token.

1. Go to the dashboard, click your domain. And swipe down until you see _Get your API Token_, click it.![image-20210108194341773](../../../AppData/Roaming/Typora/typora-user-images/image-20210108194341773.png)

![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108194424.png)

2. Create a Custom Token.![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108194514.png)

3. Do as the picture.![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108194704.png)

4. Copy the token.![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108194759.png)

5. Paste it into ~~the~~ last blank.![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108195002.png)

### Continue deploying.

5. Click `Save and Deploy`
6. If you see ![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108195119.png) that means you are OK
7. Go back to you domain's dashboard. Add a DNS Record, Type A, IP is not important, just use a placeholder.![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108195311.png)

8. Go to 'Workers' and create a route.![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108195431.png)

### Go and create a KV

1. Create a KV

![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108200012.png)

2. Bind KV![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108200204.png)

# Completed!

Go and visit your site and enjoy! Go to the management and create your first article!![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108200516.png)

![](https://cdn.jsdelivr.net/gh/orange2008/IMGBED/assets/20210108200633.png)







# ENJOY!