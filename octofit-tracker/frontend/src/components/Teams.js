import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetch('https://symmetrical-guide-65v9g9p75pg2qxx-8000.app.github.dev/api/teams/')
      .then(response => response.json())
      .then(data => setTeams(data));
  }, []);

  return (
    <div className="container mt-4">
      <h2>Teams</h2>
      <ul className="list-group">
        {teams.map(team => (
          <li key={team.id} className="list-group-item">
            {team.name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Teams;
