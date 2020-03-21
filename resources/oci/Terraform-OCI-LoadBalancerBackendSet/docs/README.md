# Terraform::OCI::LoadBalancerBackendSet

CloudFormation equivalent of oci_load_balancer_backendset

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::LoadBalancerBackendSet",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#healthchecker" title="HealthChecker">HealthChecker</a>" : <i>[ <a href="healthchecker.md">HealthChecker</a>, ... ]</i>,
        "<a href="#lbcookiesessionpersistenceconfiguration" title="LbCookieSessionPersistenceConfiguration">LbCookieSessionPersistenceConfiguration</a>" : <i>[ <a href="lbcookiesessionpersistenceconfiguration.md">LbCookieSessionPersistenceConfiguration</a>, ... ]</i>,
        "<a href="#sessionpersistenceconfiguration" title="SessionPersistenceConfiguration">SessionPersistenceConfiguration</a>" : <i>[ <a href="sessionpersistenceconfiguration.md">SessionPersistenceConfiguration</a>, ... ]</i>,
        "<a href="#sslconfiguration" title="SslConfiguration">SslConfiguration</a>" : <i>[ <a href="sslconfiguration.md">SslConfiguration</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::LoadBalancerBackendSet
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#healthchecker" title="HealthChecker">HealthChecker</a>: <i>
      - <a href="healthchecker.md">HealthChecker</a></i>
    <a href="#lbcookiesessionpersistenceconfiguration" title="LbCookieSessionPersistenceConfiguration">LbCookieSessionPersistenceConfiguration</a>: <i>
      - <a href="lbcookiesessionpersistenceconfiguration.md">LbCookieSessionPersistenceConfiguration</a></i>
    <a href="#sessionpersistenceconfiguration" title="SessionPersistenceConfiguration">SessionPersistenceConfiguration</a>: <i>
      - <a href="sessionpersistenceconfiguration.md">SessionPersistenceConfiguration</a></i>
    <a href="#sslconfiguration" title="SslConfiguration">SslConfiguration</a>: <i>
      - <a href="sslconfiguration.md">SslConfiguration</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthChecker

_Required_: No

_Type_: List of <a href="healthchecker.md">HealthChecker</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbCookieSessionPersistenceConfiguration

_Required_: No

_Type_: List of <a href="lbcookiesessionpersistenceconfiguration.md">LbCookieSessionPersistenceConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionPersistenceConfiguration

_Required_: No

_Type_: List of <a href="sessionpersistenceconfiguration.md">SessionPersistenceConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslConfiguration

_Required_: No

_Type_: List of <a href="sslconfiguration.md">SslConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Backend

Returns the <code>Backend</code> value.

#### State

Returns the <code>State</code> value.

