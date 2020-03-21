# Terraform::NSXT::LbHttpForwardingRule

CloudFormation equivalent of nsxt_lb_http_forwarding_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LbHttpForwardingRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#matchstrategy" title="MatchStrategy">MatchStrategy</a>" : <i>String</i>,
        "<a href="#bodycondition" title="BodyCondition">BodyCondition</a>" : <i>[ &lt;a href=&#34;bodycondition.md&#34;&gt;BodyCondition&lt;/a&gt;, ... ]</i>,
        "<a href="#cookiecondition" title="CookieCondition">CookieCondition</a>" : <i>[ &lt;a href=&#34;cookiecondition.md&#34;&gt;CookieCondition&lt;/a&gt;, ... ]</i>,
        "<a href="#headercondition" title="HeaderCondition">HeaderCondition</a>" : <i>[ &lt;a href=&#34;headercondition.md&#34;&gt;HeaderCondition&lt;/a&gt;, ... ]</i>,
        "<a href="#httpredirectaction" title="HttpRedirectAction">HttpRedirectAction</a>" : <i>[ &lt;a href=&#34;httpredirectaction.md&#34;&gt;HttpRedirectAction&lt;/a&gt;, ... ]</i>,
        "<a href="#httprejectaction" title="HttpRejectAction">HttpRejectAction</a>" : <i>[ &lt;a href=&#34;httprejectaction.md&#34;&gt;HttpRejectAction&lt;/a&gt;, ... ]</i>,
        "<a href="#ipcondition" title="IpCondition">IpCondition</a>" : <i>[ &lt;a href=&#34;ipcondition.md&#34;&gt;IpCondition&lt;/a&gt;, ... ]</i>,
        "<a href="#methodcondition" title="MethodCondition">MethodCondition</a>" : <i>[ &lt;a href=&#34;methodcondition.md&#34;&gt;MethodCondition&lt;/a&gt;, ... ]</i>,
        "<a href="#selectpoolaction" title="SelectPoolAction">SelectPoolAction</a>" : <i>[ &lt;a href=&#34;selectpoolaction.md&#34;&gt;SelectPoolAction&lt;/a&gt;, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;, ... ]</i>,
        "<a href="#tcpcondition" title="TcpCondition">TcpCondition</a>" : <i>[ &lt;a href=&#34;tcpcondition.md&#34;&gt;TcpCondition&lt;/a&gt;, ... ]</i>,
        "<a href="#uricondition" title="UriCondition">UriCondition</a>" : <i>[ &lt;a href=&#34;uricondition.md&#34;&gt;UriCondition&lt;/a&gt;, ... ]</i>,
        "<a href="#versioncondition" title="VersionCondition">VersionCondition</a>" : <i>[ &lt;a href=&#34;versioncondition.md&#34;&gt;VersionCondition&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LbHttpForwardingRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#matchstrategy" title="MatchStrategy">MatchStrategy</a>: <i>String</i>
    <a href="#bodycondition" title="BodyCondition">BodyCondition</a>: <i>
      - &lt;a href=&#34;bodycondition.md&#34;&gt;BodyCondition&lt;/a&gt;</i>
    <a href="#cookiecondition" title="CookieCondition">CookieCondition</a>: <i>
      - &lt;a href=&#34;cookiecondition.md&#34;&gt;CookieCondition&lt;/a&gt;</i>
    <a href="#headercondition" title="HeaderCondition">HeaderCondition</a>: <i>
      - &lt;a href=&#34;headercondition.md&#34;&gt;HeaderCondition&lt;/a&gt;</i>
    <a href="#httpredirectaction" title="HttpRedirectAction">HttpRedirectAction</a>: <i>
      - &lt;a href=&#34;httpredirectaction.md&#34;&gt;HttpRedirectAction&lt;/a&gt;</i>
    <a href="#httprejectaction" title="HttpRejectAction">HttpRejectAction</a>: <i>
      - &lt;a href=&#34;httprejectaction.md&#34;&gt;HttpRejectAction&lt;/a&gt;</i>
    <a href="#ipcondition" title="IpCondition">IpCondition</a>: <i>
      - &lt;a href=&#34;ipcondition.md&#34;&gt;IpCondition&lt;/a&gt;</i>
    <a href="#methodcondition" title="MethodCondition">MethodCondition</a>: <i>
      - &lt;a href=&#34;methodcondition.md&#34;&gt;MethodCondition&lt;/a&gt;</i>
    <a href="#selectpoolaction" title="SelectPoolAction">SelectPoolAction</a>: <i>
      - &lt;a href=&#34;selectpoolaction.md&#34;&gt;SelectPoolAction&lt;/a&gt;</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;</i>
    <a href="#tcpcondition" title="TcpCondition">TcpCondition</a>: <i>
      - &lt;a href=&#34;tcpcondition.md&#34;&gt;TcpCondition&lt;/a&gt;</i>
    <a href="#uricondition" title="UriCondition">UriCondition</a>: <i>
      - &lt;a href=&#34;uricondition.md&#34;&gt;UriCondition&lt;/a&gt;</i>
    <a href="#versioncondition" title="VersionCondition">VersionCondition</a>: <i>
      - &lt;a href=&#34;versioncondition.md&#34;&gt;VersionCondition&lt;/a&gt;</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchStrategy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BodyCondition

_Required_: No

_Type_: List of &lt;a href=&#34;bodycondition.md&#34;&gt;BodyCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieCondition

_Required_: No

_Type_: List of &lt;a href=&#34;cookiecondition.md&#34;&gt;CookieCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderCondition

_Required_: No

_Type_: List of &lt;a href=&#34;headercondition.md&#34;&gt;HeaderCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRedirectAction

_Required_: No

_Type_: List of &lt;a href=&#34;httpredirectaction.md&#34;&gt;HttpRedirectAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRejectAction

_Required_: No

_Type_: List of &lt;a href=&#34;httprejectaction.md&#34;&gt;HttpRejectAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpCondition

_Required_: No

_Type_: List of &lt;a href=&#34;ipcondition.md&#34;&gt;IpCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MethodCondition

_Required_: No

_Type_: List of &lt;a href=&#34;methodcondition.md&#34;&gt;MethodCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectPoolAction

_Required_: No

_Type_: List of &lt;a href=&#34;selectpoolaction.md&#34;&gt;SelectPoolAction&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of &lt;a href=&#34;tag.md&#34;&gt;Tag&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpCondition

_Required_: No

_Type_: List of &lt;a href=&#34;tcpcondition.md&#34;&gt;TcpCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriCondition

_Required_: No

_Type_: List of &lt;a href=&#34;uricondition.md&#34;&gt;UriCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionCondition

_Required_: No

_Type_: List of &lt;a href=&#34;versioncondition.md&#34;&gt;VersionCondition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Revision

Returns the &lt;code&gt;Revision&lt;/code&gt; value.

