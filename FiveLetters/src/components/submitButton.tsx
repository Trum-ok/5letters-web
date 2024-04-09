import enterIcon from '../assets/enter.svg';

interface SubmitButtonProps {
    attempts?: number;
    onClick?: () => void;
  }

function SubmitButton({ attempts, onClick }: SubmitButtonProps) {
  return (
    <button
            onClick={onClick}
            disabled={attempts === 0}
            style={{
              width: '30px',
              height: '30px',
              borderRadius: '5px',
              padding: '0',
              backgroundColor: attempts === 0 ? 'grey' : '#ffdd2d',
              color: 'white',
              border: 'none',
              cursor: attempts === 0 ? 'not-allowed' : 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyItems: 'center',
            }}
          >
            <img
              src={enterIcon}
              style={{
                width: '20px',
                height: '20px',
              }}
            />
    </button>
  )
}

export default SubmitButton;