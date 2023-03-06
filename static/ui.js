

// Original UI Code from
//
//  https://codepen.io/sajadhsm/pen/odaBdd
//

const SERVER_URL = window.location.href
const ANSWERS_URL = SERVER_URL + 'api/answers'

const BOT_WELCOME= "Hi, welcome to Ask me! Go ahead and ask me any question within my knowledge base. 😄"


const BOT_IMG = "/static/bot.svg";
const PERSON_IMG = "/static/you.svg";

const BOT_NAME = "Ask me Bot";
const PERSON_NAME = "You";

const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");


msgerForm.addEventListener("submit", event => {
  event.preventDefault();
  
  // Get msgText
  const msgText = msgerInput.value;
  if (!msgText) return;
  appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
  msgerInput.value = "";
  
  // Submit question
  toggleBotLoading()
  postQuestion(msgText).then((response) => {
    console.log(response); // JSON data parsed by `data.json()` call
    const answer = response.answer
    toggleBotLoading()
    botResponse(answer)

  });
})

// Example POST method implementation:
async function postQuestion(question) {
  const data =  { "question": question}
  const response = await fetch(ANSWERS_URL, {
    method: 'POST', 
    mode: 'cors', 
    cache: 'no-cache',
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', 
    body: JSON.stringify(data) 
    });
  return response.json(); 
}

botIsLoading = false
function toggleBotLoading() {
  if (botIsLoading) {
    msg = get('.left-loading-msg')
    msg.remove()
    botIsLoading = false
  } else {
    botIsLoading = true
    appendMessage(BOT_NAME, BOT_IMG, "left-loading", '...');
  }
    
}

function appendMessage(name, img, side, text) {
  //   Simple solution for small apps
    const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-img" style="background-image: url(${img})"></div>

      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>
        <div class="msg-text">${text}</div>
      </div>
    </div>
  `;

  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  msgerChat.scrollTop += 500;
}

function botResponse(msgText) {
  appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
}

// Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}

function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}


//Add welcome message  
appendMessage(BOT_NAME, BOT_IMG, "left", BOT_WELCOME);