# TF::NSXT::LbHttpForwardingRule

Provides a resource to configure lb http forwarding rule on NSX-T manager. This rule will be executed when HTTP request message is forwarded by load balancer.

~> **NOTE:** This resource requires NSX version 2.3 or higher.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::LbHttpForwardingRule",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#matchstrategy" title="MatchStrategy">MatchStrategy</a>" : <i>String</i>,
        "<a href="#bodycondition" title="BodyCondition">BodyCondition</a>" : <i>[ <a href="bodyconditiondefinition.md">BodyConditionDefinition</a>, ... ]</i>,
        "<a href="#cookiecondition" title="CookieCondition">CookieCondition</a>" : <i>[ <a href="cookieconditiondefinition.md">CookieConditionDefinition</a>, ... ]</i>,
        "<a href="#headercondition" title="HeaderCondition">HeaderCondition</a>" : <i>[ <a href="headerconditiondefinition.md">HeaderConditionDefinition</a>, ... ]</i>,
        "<a href="#httpredirectaction" title="HttpRedirectAction">HttpRedirectAction</a>" : <i>[ <a href="httpredirectactiondefinition.md">HttpRedirectActionDefinition</a>, ... ]</i>,
        "<a href="#httprejectaction" title="HttpRejectAction">HttpRejectAction</a>" : <i>[ <a href="httprejectactiondefinition.md">HttpRejectActionDefinition</a>, ... ]</i>,
        "<a href="#ipcondition" title="IpCondition">IpCondition</a>" : <i>[ <a href="ipconditiondefinition.md">IpConditionDefinition</a>, ... ]</i>,
        "<a href="#methodcondition" title="MethodCondition">MethodCondition</a>" : <i>[ <a href="methodconditiondefinition.md">MethodConditionDefinition</a>, ... ]</i>,
        "<a href="#selectpoolaction" title="SelectPoolAction">SelectPoolAction</a>" : <i>[ <a href="selectpoolactiondefinition.md">SelectPoolActionDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>,
        "<a href="#tcpcondition" title="TcpCondition">TcpCondition</a>" : <i>[ <a href="tcpconditiondefinition.md">TcpConditionDefinition</a>, ... ]</i>,
        "<a href="#uricondition" title="UriCondition">UriCondition</a>" : <i>[ <a href="uriconditiondefinition.md">UriConditionDefinition</a>, ... ]</i>,
        "<a href="#versioncondition" title="VersionCondition">VersionCondition</a>" : <i>[ <a href="versionconditiondefinition.md">VersionConditionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::LbHttpForwardingRule
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#matchstrategy" title="MatchStrategy">MatchStrategy</a>: <i>String</i>
    <a href="#bodycondition" title="BodyCondition">BodyCondition</a>: <i>
      - <a href="bodyconditiondefinition.md">BodyConditionDefinition</a></i>
    <a href="#cookiecondition" title="CookieCondition">CookieCondition</a>: <i>
      - <a href="cookieconditiondefinition.md">CookieConditionDefinition</a></i>
    <a href="#headercondition" title="HeaderCondition">HeaderCondition</a>: <i>
      - <a href="headerconditiondefinition.md">HeaderConditionDefinition</a></i>
    <a href="#httpredirectaction" title="HttpRedirectAction">HttpRedirectAction</a>: <i>
      - <a href="httpredirectactiondefinition.md">HttpRedirectActionDefinition</a></i>
    <a href="#httprejectaction" title="HttpRejectAction">HttpRejectAction</a>: <i>
      - <a href="httprejectactiondefinition.md">HttpRejectActionDefinition</a></i>
    <a href="#ipcondition" title="IpCondition">IpCondition</a>: <i>
      - <a href="ipconditiondefinition.md">IpConditionDefinition</a></i>
    <a href="#methodcondition" title="MethodCondition">MethodCondition</a>: <i>
      - <a href="methodconditiondefinition.md">MethodConditionDefinition</a></i>
    <a href="#selectpoolaction" title="SelectPoolAction">SelectPoolAction</a>: <i>
      - <a href="selectpoolactiondefinition.md">SelectPoolActionDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
    <a href="#tcpcondition" title="TcpCondition">TcpCondition</a>: <i>
      - <a href="tcpconditiondefinition.md">TcpConditionDefinition</a></i>
    <a href="#uricondition" title="UriCondition">UriCondition</a>: <i>
      - <a href="uriconditiondefinition.md">UriConditionDefinition</a></i>
    <a href="#versioncondition" title="VersionCondition">VersionCondition</a>: <i>
      - <a href="versionconditiondefinition.md">VersionConditionDefinition</a></i>
</pre>

## Properties

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this resource. Defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchStrategy

Strategy to define how load balancer rule is considered a match when multiple match conditions are specified in one rule. If set to ALL, then load balancer rule is considered a match only if all the conditions match. If set to ANY, then load balancer rule is considered a match if any one of the conditions match.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BodyCondition

_Required_: No

_Type_: List of <a href="bodyconditiondefinition.md">BodyConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieCondition

_Required_: No

_Type_: List of <a href="cookieconditiondefinition.md">CookieConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HeaderCondition

_Required_: No

_Type_: List of <a href="headerconditiondefinition.md">HeaderConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRedirectAction

_Required_: No

_Type_: List of <a href="httpredirectactiondefinition.md">HttpRedirectActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRejectAction

_Required_: No

_Type_: List of <a href="httprejectactiondefinition.md">HttpRejectActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpCondition

_Required_: No

_Type_: List of <a href="ipconditiondefinition.md">IpConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MethodCondition

_Required_: No

_Type_: List of <a href="methodconditiondefinition.md">MethodConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectPoolAction

_Required_: No

_Type_: List of <a href="selectpoolactiondefinition.md">SelectPoolActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpCondition

_Required_: No

_Type_: List of <a href="tcpconditiondefinition.md">TcpConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UriCondition

_Required_: No

_Type_: List of <a href="uriconditiondefinition.md">UriConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionCondition

_Required_: No

_Type_: List of <a href="versionconditiondefinition.md">VersionConditionDefinition</a>

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

#### Revision

Returns the <code>Revision</code> value.

