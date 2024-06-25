import style from './photoInput.module.scss'

const PhotoInput = () => {
    return (
        <div className={style.inputContainer}>
            <input type="file" id="file-upload" className={style.input} />
            <label htmlFor="file-upload" className={style.label}>
                <img src='./camera.svg' alt="photo" />
            </label>
        </div>
    )
}

export default PhotoInput;