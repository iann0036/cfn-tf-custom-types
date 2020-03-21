# Terraform::AWS::LbListenerRule

CloudFormation equivalent of aws_lb_listener_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LbListenerRule",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#listenerarn" title="ListenerArn">ListenerArn</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;, ... ]</i>,
        "<a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>" : <i>[ &lt;a href=&#34;authenticatecognito.md&#34;&gt;AuthenticateCognito&lt;/a&gt;, ... ]</i>,
        "<a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>" : <i>[ &lt;a href=&#34;authenticateoidc.md&#34;&gt;AuthenticateOidc&lt;/a&gt;, ... ]</i>,
        "<a href="#fixedresponse" title="FixedResponse">FixedResponse</a>" : <i>[ &lt;a href=&#34;fixedresponse.md&#34;&gt;FixedResponse&lt;/a&gt;, ... ]</i>,
        "<a href="#redirect" title="Redirect">Redirect</a>" : <i>[ &lt;a href=&#34;redirect.md&#34;&gt;Redirect&lt;/a&gt;, ... ]</i>,
        "<a href="#hostheader" title="HostHeader">HostHeader</a>" : <i>[ &lt;a href=&#34;hostheader.md&#34;&gt;HostHeader&lt;/a&gt;, ... ]</i>,
        "<a href="#httpheader" title="HttpHeader">HttpHeader</a>" : <i>[ &lt;a href=&#34;httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;, ... ]</i>,
        "<a href="#httprequestmethod" title="HttpRequestMethod">HttpRequestMethod</a>" : <i>[ &lt;a href=&#34;httprequestmethod.md&#34;&gt;HttpRequestMethod&lt;/a&gt;, ... ]</i>,
        "<a href="#pathpattern" title="PathPattern">PathPattern</a>" : <i>[ &lt;a href=&#34;pathpattern.md&#34;&gt;PathPattern&lt;/a&gt;, ... ]</i>,
        "<a href="#querystring" title="QueryString">QueryString</a>" : <i>[ &lt;a href=&#34;querystring.md&#34;&gt;QueryString&lt;/a&gt;, ... ]</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>[ &lt;a href=&#34;sourceip.md&#34;&gt;SourceIp&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LbListenerRule
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#listenerarn" title="ListenerArn">ListenerArn</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;</i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;</i>
    <a href="#authenticatecognito" title="AuthenticateCognito">AuthenticateCognito</a>: <i>
      - &lt;a href=&#34;authenticatecognito.md&#34;&gt;AuthenticateCognito&lt;/a&gt;</i>
    <a href="#authenticateoidc" title="AuthenticateOidc">AuthenticateOidc</a>: <i>
      - &lt;a href=&#34;authenticateoidc.md&#34;&gt;AuthenticateOidc&lt;/a&gt;</i>
    <a href="#fixedresponse" title="FixedResponse">FixedResponse</a>: <i>
      - &lt;a href=&#34;fixedresponse.md&#34;&gt;FixedResponse&lt;/a&gt;</i>
    <a href="#redirect" title="Redirect">Redirect</a>: <i>
      - &lt;a href=&#34;redirect.md&#34;&gt;Redirect&lt;/a&gt;</i>
    <a href="#hostheader" title="HostHeader">HostHeader</a>: <i>
      - &lt;a href=&#34;hostheader.md&#34;&gt;HostHeader&lt;/a&gt;</i>
    <a href="#httpheader" title="HttpHeader">HttpHeader</a>: <i>
      - &lt;a href=&#34;httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;</i>
    <a href="#httprequestmethod" title="HttpRequestMethod">HttpRequestMethod</a>: <i>
      - &lt;a href=&#34;httprequestmethod.md&#34;&gt;HttpRequestMethod&lt;/a&gt;</i>
    <a href="#pathpattern" title="PathPattern">PathPattern</a>: <i>
      - &lt;a href=&#34;pathpattern.md&#34;&gt;PathPattern&lt;/a&gt;</i>
    <a href="#querystring" title="QueryString">QueryString</a>: <i>
      - &lt;a href=&#34;querystring.md&#34;&gt;QueryString&lt;/a&gt;</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>
      - &lt;a href=&#34;sourceip.md&#34;&gt;SourceIp&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

_Type_: List of &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateCognito

_Required_: No

_Type_: List of &lt;a href=&#34;authenticatecognito.md&#34;&gt;AuthenticateCognito&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenticateOidc

_Required_: No

_Type_: List of &lt;a href=&#34;authenticateoidc.md&#34;&gt;AuthenticateOidc&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedResponse

_Required_: No

_Type_: List of &lt;a href=&#34;fixedresponse.md&#34;&gt;FixedResponse&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Redirect

_Required_: No

_Type_: List of &lt;a href=&#34;redirect.md&#34;&gt;Redirect&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostHeader

_Required_: No

_Type_: List of &lt;a href=&#34;hostheader.md&#34;&gt;HostHeader&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeader

_Required_: No

_Type_: List of &lt;a href=&#34;httpheader.md&#34;&gt;HttpHeader&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRequestMethod

_Required_: No

_Type_: List of &lt;a href=&#34;httprequestmethod.md&#34;&gt;HttpRequestMethod&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPattern

_Required_: No

_Type_: List of &lt;a href=&#34;pathpattern.md&#34;&gt;PathPattern&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryString

_Required_: No

_Type_: List of &lt;a href=&#34;querystring.md&#34;&gt;QueryString&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

_Required_: No

_Type_: List of &lt;a href=&#34;sourceip.md&#34;&gt;SourceIp&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

