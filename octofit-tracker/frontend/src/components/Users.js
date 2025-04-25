import React, { useEffect, useState } from 'react';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://symmetrical-guide-65v9g9p75pg2qxx-8000.app.github.dev/api/users/')
      .then(response => response.json())
      .then(data => setUsers(data));
  }, []);

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <ul className="list-group">
        {users.map(user => (
          <li key={user.id} className="list-group-item">
            {user.username}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Users;
