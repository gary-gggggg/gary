console.log('外部JS加载成功')
console.log(blogData);
console.log(faderData);

$(function(){
  //当页面加载完成后执行的代码
  // 图片路劲千万不要写死
  var Base_Url='../project/static/images/';
  //遍历faderdata 生成3个li标签 添加到页面元素.faderdate之前
  var html=''
  $.each(faderData,function(i,o){
    html+=`<li class="slide">
            <a href="#">
              <img src="${Base_Url+o.img_url}">
              <span class="imginfo">
              ${o.img_info}
              </span>
            </a>
          </li>`    
        })
  $('.fader_controls').before(html);
  $('.fader').easyFader();
  









})