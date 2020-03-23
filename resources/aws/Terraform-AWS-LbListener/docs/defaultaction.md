# Terraform::AWS::LbListener DefaultAction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
    "<a href="#targetgrouparn" title="TargetGroupArn">TargetGroupArn</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>" : <i>[ <a href="defaultaction-authenticatecognito.md">AuthenticateCognito</a>, ... ]</i>,
    "<a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>" : <i>[ <a href="defaultaction-authenticateoidc.md">AuthenticateOidc</a>, ... ]</i>,
    "<a href="#fixedresponse" title="FixedResponse">FixedResponse</a>" : <i>[ <a href="defaultaction-fixedresponse.md">FixedResponse</a>, ... ]</i>,
    "<a href="#redirect" title="Redirect">Redirect</a>" : <i>[ <a href="defaultaction-redirect.md">Redirect</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#order" title="Order">Order</a>: <i>Double</i>
<a href="#targetgrouparn" title="TargetGroupArn">TargetGroupArn</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>: <i>
      - <a href="defaultaction-authenticatecognito.md">AuthenticateCognito</a></i>
<a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>: <i>
      - <a href="defaultaction-authenticateoidc.md">AuthenticateOidc</a></i>
<a href="#fixedresponse" title="FixedResponse">FixedResponse</a>: <i>
      - <a href="defaultaction-fixedresponse.md">FixedResponse</a></i>
<a href="#redirect" title="Redirect">Redirect</a>: <i>
      - <a href="defaultaction-redirect.md">Redirect</a></i>
</pre>

## Properties

#### Order

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupArn

The ARN of the Target Group to which to route traffic. Required if `type` is `forward`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of routing action. Valid values are `forward`, `redirect`, `fixed-response`, `authenticate-cognito` and `authenticate-oidc`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateCognito

_Required_: No

_Type_: List of <a href="defaultaction-authenticatecognito.md">AuthenticateCognito</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateOidc

_Required_: No

_Type_: List of <a href="defaultaction-authenticateoidc.md">AuthenticateOidc</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedResponse

_Required_: No

_Type_: List of <a href="defaultaction-fixedresponse.md">FixedResponse</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redirect

_Required_: No

_Type_: List of <a href="defaultaction-redirect.md">Redirect</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

