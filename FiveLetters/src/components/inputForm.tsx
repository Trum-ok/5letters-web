interface InputFormProps {
  index: number;
  value: string;
  hIC: (index: number, event: any) => void;
  hKD: (index: number, event: any) => void;
  iRefs: { [key: number]: HTMLInputElement; };
}

const InputForm = ({ index, value, hIC, hKD, iRefs }: InputFormProps) => {
  return (
    <input
      key={index}
      type="text"
      pattern='[а-яА-Я]+'
      value={value}
      onChange={(event) => hIC(index, event)}
      onKeyDown={(event) => hKD(index, event)}
      maxLength={1}
      ref={(input) => (iRefs.current[index] = input)}
      style={{
        marginRight: '5px',
        height: '50px',
        width: '50px',
        textAlign: 'center',
        borderRadius: '5px',
        boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
        border: 'none',
        outline: 'none',
      }}
      onFocus={() => {
        iRefs.current[index].style.boxShadow = '0 0 2px 1px white';
      }}
      onBlur={() => {
        iRefs.current[index].style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
      }}
    />
  );
};

export default InputForm;