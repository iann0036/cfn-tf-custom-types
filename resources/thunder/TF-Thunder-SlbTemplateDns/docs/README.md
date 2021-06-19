# TF::Thunder::SlbTemplateDns

`thunder_slb_template_dns` Provides details about thunder slb template dns

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateDns",
    "Properties" : {
        "<a href="#defaultpolicy" title="DefaultPolicy">DefaultPolicy</a>" : <i>String</i>,
        "<a href="#disablednstemplate" title="DisableDnsTemplate">DisableDnsTemplate</a>" : <i>Double</i>,
        "<a href="#dnssecservicegroup" title="DnssecServiceGroup">DnssecServiceGroup</a>" : <i>String</i>,
        "<a href="#drop" title="Drop">Drop</a>" : <i>Double</i>,
        "<a href="#enablecachesharing" title="EnableCacheSharing">EnableCacheSharing</a>" : <i>Double</i>,
        "<a href="#forward" title="Forward">Forward</a>" : <i>String</i>,
        "<a href="#maxcacheentrysize" title="MaxCacheEntrySize">MaxCacheEntrySize</a>" : <i>Double</i>,
        "<a href="#maxcachesize" title="MaxCacheSize">MaxCacheSize</a>" : <i>Double</i>,
        "<a href="#maxquerylength" title="MaxQueryLength">MaxQueryLength</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#queryidswitch" title="QueryIdSwitch">QueryIdSwitch</a>" : <i>Double</i>,
        "<a href="#redirecttotcpport" title="RedirectToTcpPort">RedirectToTcpPort</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#classlist" title="ClassList">ClassList</a>" : <i>[ <a href="classlistdefinition.md">ClassListDefinition</a>, ... ]</i>,
        "<a href="#responseratelimiting" title="ResponseRateLimiting">ResponseRateLimiting</a>" : <i>[ <a href="responseratelimitingdefinition.md">ResponseRateLimitingDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateDns
Properties:
    <a href="#defaultpolicy" title="DefaultPolicy">DefaultPolicy</a>: <i>String</i>
    <a href="#disablednstemplate" title="DisableDnsTemplate">DisableDnsTemplate</a>: <i>Double</i>
    <a href="#dnssecservicegroup" title="DnssecServiceGroup">DnssecServiceGroup</a>: <i>String</i>
    <a href="#drop" title="Drop">Drop</a>: <i>Double</i>
    <a href="#enablecachesharing" title="EnableCacheSharing">EnableCacheSharing</a>: <i>Double</i>
    <a href="#forward" title="Forward">Forward</a>: <i>String</i>
    <a href="#maxcacheentrysize" title="MaxCacheEntrySize">MaxCacheEntrySize</a>: <i>Double</i>
    <a href="#maxcachesize" title="MaxCacheSize">MaxCacheSize</a>: <i>Double</i>
    <a href="#maxquerylength" title="MaxQueryLength">MaxQueryLength</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#queryidswitch" title="QueryIdSwitch">QueryIdSwitch</a>: <i>Double</i>
    <a href="#redirecttotcpport" title="RedirectToTcpPort">RedirectToTcpPort</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#classlist" title="ClassList">ClassList</a>: <i>
      - <a href="classlistdefinition.md">ClassListDefinition</a></i>
    <a href="#responseratelimiting" title="ResponseRateLimiting">ResponseRateLimiting</a>: <i>
      - <a href="responseratelimitingdefinition.md">ResponseRateLimitingDefinition</a></i>
</pre>

## Properties

#### DefaultPolicy

‘nocache’: Cache disable; ‘cache’: Cache enable;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableDnsTemplate

Disable DNS template.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnssecServiceGroup

Use different service group if DNSSEC DO bit set (Service Group Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Drop

Drop the malformed query.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCacheSharing

Enable DNS cache sharing.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Forward

Forward to service group (Service group name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCacheEntrySize

Define maximum cache entry size (Maximum cache entry size per VIP).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCacheSize

Define maximum cache size (Maximum cache entry per VIP).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxQueryLength

Define Maximum DNS Query Length, default is unlimited (Specify Maximum Length).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specify a class list name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

Period in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueryIdSwitch

Use DNS query ID to create sesion.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectToTcpPort

Direct the client to retry with TCP for DNS UDP request.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassList

_Required_: No

_Type_: List of <a href="classlistdefinition.md">ClassListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseRateLimiting

_Required_: No

_Type_: List of <a href="responseratelimitingdefinition.md">ResponseRateLimitingDefinition</a>

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

