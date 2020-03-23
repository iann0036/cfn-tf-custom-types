# Terraform::AWS::LbCookieStickinessPolicy

Provides a load balancer cookie stickiness policy, which allows an ELB to control the sticky session lifetime of the browser.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LbCookieStickinessPolicy",
    "Properties" : {
        "<a href="#cookieexpirationperiod" title="CookieExpirationPeriod">CookieExpirationPeriod</a>" : <i>Double</i>,
        "<a href="#lbport" title="LbPort">LbPort</a>" : <i>Double</i>,
        "<a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LbCookieStickinessPolicy
Properties:
    <a href="#cookieexpirationperiod" title="CookieExpirationPeriod">CookieExpirationPeriod</a>: <i>Double</i>
    <a href="#lbport" title="LbPort">LbPort</a>: <i>Double</i>
    <a href="#loadbalancer" title="LoadBalancer">LoadBalancer</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### CookieExpirationPeriod

The time period after which
the session cookie should be considered stale, expressed in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbPort

The load balancer port to which the policy
should be applied. This must be an active listener on the load
balancer.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancer

The load balancer to which the policy
should be attached.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the stickiness policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

