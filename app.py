import streamlit as st
from PIL import Image, ImageFilter, ImageEnhance
import os
from datetime import datetime
# 깃 연동 했음
def load_image(image_file) :
    img = Image.open(image_file)
    return img

# 디렉토리와 이미지를 주면, 해당 디렉토리에 이 이미지를 저장하는 함수
def save_uploaded_file(directory, img):
    # 1. 디렉토리가 있는지 확인하여, 없으면 만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 이제는 디렉토리가 있으니까, 파일을 저장.
    
    filename = datetime.now().isoformat().replace(':','-').replace('.','-')
    
    img.save(directory+'/'+filename+'.jpg')
    return st.success('Saved file : {} in {}'.format(filename+'.jpg',directory))

def main():

    # 1. 파일을 업로드하기.
    image_file_list = st.file_uploader('Upload Image',type=['png','jpg','jpeg'],accept_multiple_files=True)

    print(image_file_list)

    if image_file_list is not None :

        # 2. 각 파일을 이미지로 바꿔줘야 한다.
        image_list = []

        # 2-1. 모든 파일이, image_list에 이미지로 저장됨
        for image_file in image_file_list :
            img = load_image(image_file)
            image_list.append(img)

        # 3. 이미지를 화면에 확인해 본다
        # for img in image_list :
        #     st.image(img)

        option_list = ['Show Image','Rotate Image','Create Thumbnail','Crop Image','Merge Images','Flip Image','Change Color','Filters - Sharpen','Filters - Edge Enhance','Contrast Image']
        option = st.selectbox('옵션을 선택하세요.',option_list)

            # 2. 하드 코딩을 없애는 작업
    
        if option == 'Show Image' :
            for img in image_list :
                st.image(img)

            directory = st.text_input('파일 경로 입력')
            if st.button('파일 저장') :
                # 3. 파일 저장.
                for img in image_list :
                    save_uploaded_file(directory, img)

        elif option == 'Rotate Image' :
            # 1. 유저가 입력
            degree = st.number_input('각도 입력',0,360)

            # 2. 모든 이미지를 돌려본다.
            transformed_img_list = []
            for img in image_list :
                rotated_img = img.rotate(degree)
                st.image(rotated_img)
                transformed_img_list.append(rotated_img)

            directory = st.text_input('파일 경로 입력')
            if st.button('파일 저장') :
                # 3. 파일 저장.
                for img in transformed_img_list :
                    save_uploaded_file(directory, img)


        elif option == 'Create Thumbnail' :
            # 1. 이미지의 사이즈를 알아야겠다.
            
            width = st.number_input('width 입력',1,100)
            height = st.number_input('height 입력',1,100)
            size = (width,height)
            transformed_img_list = []

            for img in image_list :
                img.thumbnail(size)
                st.image(img)
                transformed_img_list.append(img)

            # 저장은 여기서
            directory = st.text_input('파일 경로 입력')
            if st.button('파일 저장') :
                # 3. 파일 저장.
                for img in transformed_img_list :
                    save_uploaded_file(directory, img)

    #    elif option == 'Crop Image' :
    #        # 왼쪽 윗부분 부터 시작해서, 너비와 깊이 만큼 잘라라
    #        # 왼쪽 윗부분 좌표 (50,100)
    #        # 너비 x축으로, 깊이 y축으로 계산한 종료 좌표 (200,200)
    #        # 시작좌표 + (너비,높이) => 크랍 종료 좌표
            
    #        start_x = st.number_input('시작 x 좌표',1,img.size[0]-1)
    #        start_y = st.number_input('시작 y 좌표',1,img.size[1]-1)
    #        max_width = img.size[0] - start_x
    #        max_height = img.size[1] - start_y
    #        width = st.number_input('width 입력',1,max_width)
    #        height = st.number_input('height 입력',1,max_height)

    #        box = (start_x,start_y,start_x+width, start_y+height)
    #        st.write(box)
    #        cropped_img = img.crop(box)
    #        # cropped_img.save('data/crop.png')
    #        st.image(cropped_img)

    #    elif option == 'Merge Images' :

    #        merge_file = st.file_uploader('Upload Image',type=['png','jpg','jpeg'],key='merge')

    #        if merge_file is not None :

    #            merge_img = load_image(merge_file)

    #            start_x = st.number_input('시작 x 좌표',1,img.size[0]-1)
    #            start_y = st.number_input('시작 y 좌표',1,img.size[1]-1)

    #            position = (start_x,start_y)
    #            img.paste(merge_img,position)
    #            st.image(img)

        elif option == 'Flip Image' :
            status = st.radio('플립 선택',['FLIP_TOP_BOTTOM','FLIP_LEFT_RIGHT'])
            if status == 'FLIP_TOP_BOTTOM' :
                transformed_img_list = []
                for img in image_list :
                    flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)

            elif status == 'FLIP_LEFT_RIGHT' :
                transformed_img_list = []
                for img in image_list :
                    flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                    st.image(flipped_img)
                    transformed_img_list.append(flipped_img)
            

            
            # 3. 파일 저장.
            for img in transformed_img_list :
                save_uploaded_file(directory, img)



    #     elif option == 'Change Color' :
    #         status = st.radio('색 변경',['Color','Gray Scale','Black & White'])

    #         if status == 'Color' :
    #             color = 'RGB'
    #         elif status == 'Gray Scale' :
    #             color = 'L'
    #         elif status == 'Black & White' :
    #             color = '1'

    #         bw = img.convert(color)
    #         st.image(bw)

    #     elif option == 'Filters - Sharpen' :
    #         sharp_img = img.filter(ImageFilter.SHARPEN)
    #         st.image(sharp_img)

    #     elif option == 'Filters - Edge Enhance' :
    #         edge_img = img.filter(ImageFilter.EDGE_ENHANCE)
    #         st.image(edge_img)

    #     elif option == 'Contrast Image' :
    #         contrast_img = ImageEnhance.Contrast(img).enhance(2)
    #         st.image(contrast_img) 

if __name__=='__main__':
    main()