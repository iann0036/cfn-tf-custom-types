# Terraform::AWS::AlbListenerRule

CloudFormation equivalent of aws_alb_listener_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::AlbListenerRule",
    "Properties" : {
        "<a href="#listenerarn" title="ListenerArn">ListenerArn</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ <a href="action.md">Action</a>, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="condition.md">Condition</a>, ... ]</i>,
        "<a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>" : <i>[ <a href="authenticatecognito.md">AuthenticateCognito</a>, ... ]</i>,
        "<a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>" : <i>[ <a href="authenticateoidc.md">AuthenticateOidc</a>, ... ]</i>,
        "<a href="#fixedresponse" title="FixedResponse">FixedResponse</a>" : <i>[ <a href="fixedresponse.md">FixedResponse</a>, ... ]</i>,
        "<a href="#redirect" title="Redirect">Redirect</a>" : <i>[ <a href="redirect.md">Redirect</a>, ... ]</i>,
        "<a href="#hostheader" title="HostHeader">HostHeader</a>" : <i>[ <a href="hostheader.md">HostHeader</a>, ... ]</i>,
        "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>[ <a href="httpheader.md">HttpHeader</a>, ... ]</i>,
        "<a href="#httprequestmethod" title="HttpRequestMethod">HttpRequestMethod</a>" : <i>[ <a href="httprequestmethod.md">HttpRequestMethod</a>, ... ]</i>,
        "<a href="#pathpattern" title="PathPattern">PathPattern</a>" : <i>[ <a href="pathpattern.md">PathPattern</a>, ... ]</i>,
        "<a href="#querystring" title="QueryString">QueryString</a>" : <i>[ <a href="querystring.md">QueryString</a>, ... ]</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>[ <a href="sourceip.md">SourceIp</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::AlbListenerRule
Properties:
    <a href="#listenerarn" title="ListenerArn">ListenerArn</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#action" title="Action">Action</a>: <i>
      - <a href="action.md">Action</a></i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="condition.md">Condition</a></i>
    <a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>: <i>
      - <a href="authenticatecognito.md">AuthenticateCognito</a></i>
    <a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>: <i>
      - <a href="authenticateoidc.md">AuthenticateOidc</a></i>
    <a href="#fixedresponse" title="FixedResponse">FixedResponse</a>: <i>
      - <a href="fixedresponse.md">FixedResponse</a></i>
    <a href="#redirect" title="Redirect">Redirect</a>: <i>
      - <a href="redirect.md">Redirect</a></i>
    <a href="#hostheader" title="HostHeader">HostHeader</a>: <i>
      - <a href="hostheader.md">HostHeader</a></i>
    <a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>
      - <a href="httpheader.md">HttpHeader</a></i>
    <a href="#httprequestmethod" title="HttpRequestMethod">HttpRequestMethod</a>: <i>
      - <a href="httprequestmethod.md">HttpRequestMethod</a></i>
    <a href="#pathpattern" title="PathPattern">PathPattern</a>: <i>
      - <a href="pathpattern.md">PathPattern</a></i>
    <a href="#querystring" title="QueryString">QueryString</a>: <i>
      - <a href="querystring.md">QueryString</a></i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>
      - <a href="sourceip.md">SourceIp</a></i>
</pre>

## Properties

#### ListenerArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of <a href="action.md">Action</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="condition.md">Condition</a>

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

#### HostHeader

_Required_: No

_Type_: List of <a href="hostheader.md">HostHeader</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No

_Type_: List of <a href="httpheader.md">HttpHeader</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestMethod

_Required_: No

_Type_: List of <a href="httprequestmethod.md">HttpRequestMethod</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPattern

_Required_: No

_Type_: List of <a href="pathpattern.md">PathPattern</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

_Required_: No

_Type_: List of <a href="querystring.md">QueryString</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

_Required_: No

_Type_: List of <a href="sourceip.md">SourceIp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

