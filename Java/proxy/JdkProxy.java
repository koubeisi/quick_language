// package proxy

import java.lang.reflect.Proxy;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.util.Arrays;

/**
 * @author koubs
 * @date 2020/12/6
 */
public class JdkProxy {

    public static void main(String[] args) {
        var userDao = new UserDaoImpl();
        var proxy = new UserDaoProxy(userDao).getInstance();
        var i = proxy.add(1, 2);
        System.out.println(i);
    }
}


interface UserDao {

    int add(int a,int b);
}

class UserDaoImpl implements UserDao{
    @Override
    public int add(int a, int b) {
        System.out.println("方法执行中");
        return a+b;
    }
}

class UserDaoProxy implements InvocationHandler {

    private UserDao userDao;

    public UserDaoProxy(UserDao userDao){
        this.userDao = userDao;
    }

    public UserDao getInstance(){
        return (UserDao)Proxy.newProxyInstance(userDao.getClass().getClassLoader(), userDao.getClass().getInterfaces(), this);
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // 方法之前
        System.out.printf("方法之前执行：%s,传递的参数：%s",method.getName(), Arrays.toString(args));

        // 被增强方法执行
        Object result = method.invoke(userDao, args);

        // 方法之后
        System.out.println("方法执行之后");

        return result;
    }
}

