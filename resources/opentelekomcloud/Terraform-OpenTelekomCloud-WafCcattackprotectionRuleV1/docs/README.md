# Terraform::OpenTelekomCloud::WafCcattackprotectionRuleV1

Manages a WAF CC Attack Protection Rule resource within OpenTelekomCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::WafCcattackprotectionRuleV1",
    "Properties" : {
        "<a href="#actioncategory" title="ActionCategory">ActionCategory</a>" : <i>String</i>,
        "<a href="#blockcontent" title="BlockContent">BlockContent</a>" : <i>String</i>,
        "<a href="#blockcontenttype" title="BlockContentType">BlockContentType</a>" : <i>String</i>,
        "<a href="#limitnum" title="LimitNum">LimitNum</a>" : <i>Double</i>,
        "<a href="#limitperiod" title="LimitPeriod">LimitPeriod</a>" : <i>Double</i>,
        "<a href="#locktime" title="LockTime">LockTime</a>" : <i>Double</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>String</i>,
        "<a href="#tagcategory" title="TagCategory">TagCategory</a>" : <i>String</i>,
        "<a href="#tagcontents" title="TagContents">TagContents</a>" : <i>[ String, ... ]</i>,
        "<a href="#tagindex" title="TagIndex">TagIndex</a>" : <i>String</i>,
        "<a href="#tagtype" title="TagType">TagType</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::WafCcattackprotectionRuleV1
Properties:
    <a href="#actioncategory" title="ActionCategory">ActionCategory</a>: <i>String</i>
    <a href="#blockcontent" title="BlockContent">BlockContent</a>: <i>String</i>
    <a href="#blockcontenttype" title="BlockContentType">BlockContentType</a>: <i>String</i>
    <a href="#limitnum" title="LimitNum">LimitNum</a>: <i>Double</i>
    <a href="#limitperiod" title="LimitPeriod">LimitPeriod</a>: <i>Double</i>
    <a href="#locktime" title="LockTime">LockTime</a>: <i>Double</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>String</i>
    <a href="#tagcategory" title="TagCategory">TagCategory</a>: <i>String</i>
    <a href="#tagcontents" title="TagContents">TagContents</a>: <i>
      - String</i>
    <a href="#tagindex" title="TagIndex">TagIndex</a>: <i>String</i>
    <a href="#tagtype" title="TagType">TagType</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### ActionCategory

Specifies the action. Changing this creates a new rule. Valid Options are:
* `block` - block the requests.
* `captcha` - Verification code. The user needs to enter the correct verification code after blocking to restore the correct access page.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockContent

Specifies the content of the returned page. Changing this creates a new rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockContentType

Specifies the type of the returned page. The options are `application/json`, `text/html`, and `text/xml`. Changing this creates a new rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitNum

Specifies the number of requests allowed from a web visitor in a rate limiting period. Changing this creates a new rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitPeriod

Specifies the rate limiting period. Changing this creates a new rule.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LockTime

Specifies the lock duration. The value ranges from 0 seconds to 2^32 seconds. Changing this creates a new rule.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

The WAF policy ID. Changing this creates a new rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagCategory

Specifies the category. The value is `referer`. Changing this creates a new rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagContents

Specifies the category content. Changing this creates a new rule.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagIndex

If `tag_type` is set to `cookie`, this parameter indicates cookie name. Changing this creates a new rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagType

Specifies the rate limit mode. Changing this creates a new rule. Valid Options are:
* `ip` - A web visitor is identified by the IP address.
* `cookie` - A web visitor is identified by the cookie key value.
* `other` - A web visitor is identified by the Referer field(user-defined request source).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

Specifies a misreported URL excluding a domain name. Changing this creates a new rule.

_Required_: Yes

_Type_: String

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

#### Default

Returns the <code>Default</code> value.

