# Terraform::NSXT::LbHttpRequestRewriteRule

CloudFormation equivalent of nsxt_lb_http_request_rewrite_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LbHttpRequestRewriteRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#matchstrategy" title="MatchStrategy">MatchStrategy</a>" : <i>String</i>,
        "<a href="#bodycondition" title="BodyCondition">BodyCondition</a>" : <i>[ <a href="bodycondition.md">BodyCondition</a>, ... ]</i>,
        "<a href="#cookiecondition" title="CookieCondition">CookieCondition</a>" : <i>[ <a href="cookiecondition.md">CookieCondition</a>, ... ]</i>,
        "<a href="#headercondition" title="HeaderCondition">HeaderCondition</a>" : <i>[ <a href="headercondition.md">HeaderCondition</a>, ... ]</i>,
        "<a href="#headerrewriteaction" title="HeaderRewriteAction">HeaderRewriteAction</a>" : <i>[ <a href="headerrewriteaction.md">HeaderRewriteAction</a>, ... ]</i>,
        "<a href="#ipcondition" title="IpCondition">IpCondition</a>" : <i>[ <a href="ipcondition.md">IpCondition</a>, ... ]</i>,
        "<a href="#methodcondition" title="MethodCondition">MethodCondition</a>" : <i>[ <a href="methodcondition.md">MethodCondition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>,
        "<a href="#tcpcondition" title="TcpCondition">TcpCondition</a>" : <i>[ <a href="tcpcondition.md">TcpCondition</a>, ... ]</i>,
        "<a href="#uriargumentscondition" title="UriArgumentsCondition">UriArgumentsCondition</a>" : <i>[ <a href="uriargumentscondition.md">UriArgumentsCondition</a>, ... ]</i>,
        "<a href="#uricondition" title="UriCondition">UriCondition</a>" : <i>[ <a href="uricondition.md">UriCondition</a>, ... ]</i>,
        "<a href="#urirewriteaction" title="UriRewriteAction">UriRewriteAction</a>" : <i>[ <a href="urirewriteaction.md">UriRewriteAction</a>, ... ]</i>,
        "<a href="#versioncondition" title="VersionCondition">VersionCondition</a>" : <i>[ <a href="versioncondition.md">VersionCondition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LbHttpRequestRewriteRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#matchstrategy" title="MatchStrategy">MatchStrategy</a>: <i>String</i>
    <a href="#bodycondition" title="BodyCondition">BodyCondition</a>: <i>
      - <a href="bodycondition.md">BodyCondition</a></i>
    <a href="#cookiecondition" title="CookieCondition">CookieCondition</a>: <i>
      - <a href="cookiecondition.md">CookieCondition</a></i>
    <a href="#headercondition" title="HeaderCondition">HeaderCondition</a>: <i>
      - <a href="headercondition.md">HeaderCondition</a></i>
    <a href="#headerrewriteaction" title="HeaderRewriteAction">HeaderRewriteAction</a>: <i>
      - <a href="headerrewriteaction.md">HeaderRewriteAction</a></i>
    <a href="#ipcondition" title="IpCondition">IpCondition</a>: <i>
      - <a href="ipcondition.md">IpCondition</a></i>
    <a href="#methodcondition" title="MethodCondition">MethodCondition</a>: <i>
      - <a href="methodcondition.md">MethodCondition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
    <a href="#tcpcondition" title="TcpCondition">TcpCondition</a>: <i>
      - <a href="tcpcondition.md">TcpCondition</a></i>
    <a href="#uriargumentscondition" title="UriArgumentsCondition">UriArgumentsCondition</a>: <i>
      - <a href="uriargumentscondition.md">UriArgumentsCondition</a></i>
    <a href="#uricondition" title="UriCondition">UriCondition</a>: <i>
      - <a href="uricondition.md">UriCondition</a></i>
    <a href="#urirewriteaction" title="UriRewriteAction">UriRewriteAction</a>: <i>
      - <a href="urirewriteaction.md">UriRewriteAction</a></i>
    <a href="#versioncondition" title="VersionCondition">VersionCondition</a>: <i>
      - <a href="versioncondition.md">VersionCondition</a></i>
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

#### MatchStrategy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BodyCondition

_Required_: No

_Type_: List of <a href="bodycondition.md">BodyCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieCondition

_Required_: No

_Type_: List of <a href="cookiecondition.md">CookieCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderCondition

_Required_: No

_Type_: List of <a href="headercondition.md">HeaderCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderRewriteAction

_Required_: No

_Type_: List of <a href="headerrewriteaction.md">HeaderRewriteAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpCondition

_Required_: No

_Type_: List of <a href="ipcondition.md">IpCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MethodCondition

_Required_: No

_Type_: List of <a href="methodcondition.md">MethodCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpCondition

_Required_: No

_Type_: List of <a href="tcpcondition.md">TcpCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriArgumentsCondition

_Required_: No

_Type_: List of <a href="uriargumentscondition.md">UriArgumentsCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriCondition

_Required_: No

_Type_: List of <a href="uricondition.md">UriCondition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriRewriteAction

_Required_: No

_Type_: List of <a href="urirewriteaction.md">UriRewriteAction</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionCondition

_Required_: No

_Type_: List of <a href="versioncondition.md">VersionCondition</a>

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

Returns the <code>Revision</code> value.

