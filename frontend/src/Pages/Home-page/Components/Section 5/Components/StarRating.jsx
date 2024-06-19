import ReactStars from 'react-rating-stars-component';

const StarRating = () => {

  

  return (
    <div>
      <ReactStars
        count={5}
        size={30}
        activeColor="#ffd700"
      />
    </div>
  );
};

export default StarRating;