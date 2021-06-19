# TF::AWS::LbListenerRule ActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
    "<a href="#targetgrouparn" title="TargetGroupArn">TargetGroupArn</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>" : <i>[ <a href="authenticatecognitodefinition.md">AuthenticateCognitoDefinition</a>, ... ]</i>,
    "<a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>" : <i>[ <a href="authenticateoidcdefinition.md">AuthenticateOidcDefinition</a>, ... ]</i>,
    "<a href="#fixedresponse" title="FixedResponse">FixedResponse</a>" : <i>[ <a href="fixedresponsedefinition.md">FixedResponseDefinition</a>, ... ]</i>,
    "<a href="#forward" title="Forward">Forward</a>" : <i>[ <a href="forwarddefinition.md">ForwardDefinition</a>, ... ]</i>,
    "<a href="#redirect" title="Redirect">Redirect</a>" : <i>[ <a href="redirectdefinition.md">RedirectDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#order" title="Order">Order</a>: <i>Double</i>
<a href="#targetgrouparn" title="TargetGroupArn">TargetGroupArn</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>: <i>
      - <a href="authenticatecognitodefinition.md">AuthenticateCognitoDefinition</a></i>
<a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>: <i>
      - <a href="authenticateoidcdefinition.md">AuthenticateOidcDefinition</a></i>
<a href="#fixedresponse" title="FixedResponse">FixedResponse</a>: <i>
      - <a href="fixedresponsedefinition.md">FixedResponseDefinition</a></i>
<a href="#forward" title="Forward">Forward</a>: <i>
      - <a href="forwarddefinition.md">ForwardDefinition</a></i>
<a href="#redirect" title="Redirect">Redirect</a>: <i>
      - <a href="redirectdefinition.md">RedirectDefinition</a></i>
</pre>

## Properties

#### Order

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateCognito

_Required_: No

_Type_: List of <a href="authenticatecognitodefinition.md">AuthenticateCognitoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateOidc

_Required_: No

_Type_: List of <a href="authenticateoidcdefinition.md">AuthenticateOidcDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedResponse

_Required_: No

_Type_: List of <a href="fixedresponsedefinition.md">FixedResponseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forward

_Required_: No

_Type_: List of <a href="forwarddefinition.md">ForwardDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redirect

_Required_: No

_Type_: List of <a href="redirectdefinition.md">RedirectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

