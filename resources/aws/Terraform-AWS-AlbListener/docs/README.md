# Terraform::AWS::AlbListener

CloudFormation equivalent of aws_alb_listener

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AlbListener",
    "Properties" : {
        "<a href="#certificatearn" title="CertificateArn">CertificateArn</a>" : <i>String</i>,
        "<a href="#loadbalancerarn" title="LoadBalancerArn">LoadBalancerArn</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#sslpolicy" title="SslPolicy">SslPolicy</a>" : <i>String</i>,
        "<a href="#defaultaction" title="DefaultAction">DefaultAction</a>" : <i>[ <a href="defaultaction.md">DefaultAction</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>" : <i>[ <a href="authenticatecognito.md">AuthenticateCognito</a>, ... ]</i>,
        "<a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>" : <i>[ <a href="authenticateoidc.md">AuthenticateOidc</a>, ... ]</i>,
        "<a href="#fixedresponse" title="FixedResponse">FixedResponse</a>" : <i>[ <a href="fixedresponse.md">FixedResponse</a>, ... ]</i>,
        "<a href="#redirect" title="Redirect">Redirect</a>" : <i>[ <a href="redirect.md">Redirect</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AlbListener
Properties:
    <a href="#certificatearn" title="CertificateArn">CertificateArn</a>: <i>String</i>
    <a href="#loadbalancerarn" title="LoadBalancerArn">LoadBalancerArn</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#sslpolicy" title="SslPolicy">SslPolicy</a>: <i>String</i>
    <a href="#defaultaction" title="DefaultAction">DefaultAction</a>: <i>
      - <a href="defaultaction.md">DefaultAction</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>: <i>
      - <a href="authenticatecognito.md">AuthenticateCognito</a></i>
    <a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>: <i>
      - <a href="authenticateoidc.md">AuthenticateOidc</a></i>
    <a href="#fixedresponse" title="FixedResponse">FixedResponse</a>: <i>
      - <a href="fixedresponse.md">FixedResponse</a></i>
    <a href="#redirect" title="Redirect">Redirect</a>: <i>
      - <a href="redirect.md">Redirect</a></i>
</pre>

## Properties

#### CertificateArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAction

_Required_: No

_Type_: List of <a href="defaultaction.md">DefaultAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateCognito

_Required_: No

_Type_: List of <a href="authenticatecognito.md">AuthenticateCognito</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateOidc

_Required_: No

_Type_: List of <a href="authenticateoidc.md">AuthenticateOidc</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedResponse

_Required_: No

_Type_: List of <a href="fixedresponse.md">FixedResponse</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redirect

_Required_: No

_Type_: List of <a href="redirect.md">Redirect</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

