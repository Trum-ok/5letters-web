interface ToggleTypewriterProps {
  toggleTypewriter: () => void;
  isTypewriterActive: boolean;
  styles: React.CSSProperties;
}

const ToggleTypewriter = ({ toggleTypewriter, isTypewriterActive, styles }: ToggleTypewriterProps) => {
  return (
    <div className="togler" style={styles}>
      <label>
        <input
          type="checkbox"
          onChange={ toggleTypewriter}
          checked={!isTypewriterActive}
        />
        Отключить анимацию
      </label>
    </div>
  );
};

export default ToggleTypewriter;