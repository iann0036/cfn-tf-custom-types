# TF::TencentCloud::CdnDomain

Provides a resource to create a CDN domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::CdnDomain",
    "Properties" : {
        "<a href="#area" title="Area">Area</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#fullurlcache" title="FullUrlCache">FullUrlCache</a>" : <i>Boolean</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#rangeoriginswitch" title="RangeOriginSwitch">RangeOriginSwitch</a>" : <i>String</i>,
        "<a href="#servicetype" title="ServiceType">ServiceType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#httpsconfig" title="HttpsConfig">HttpsConfig</a>" : <i>[ <a href="httpsconfigdefinition.md">HttpsConfigDefinition</a>, ... ]</i>,
        "<a href="#origin" title="Origin">Origin</a>" : <i>[ <a href="origindefinition.md">OriginDefinition</a>, ... ]</i>,
        "<a href="#requestheader" title="RequestHeader">RequestHeader</a>" : <i>[ <a href="requestheaderdefinition.md">RequestHeaderDefinition</a>, ... ]</i>,
        "<a href="#rulecache" title="RuleCache">RuleCache</a>" : <i>[ <a href="rulecachedefinition.md">RuleCacheDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::CdnDomain
Properties:
    <a href="#area" title="Area">Area</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#fullurlcache" title="FullUrlCache">FullUrlCache</a>: <i>Boolean</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#rangeoriginswitch" title="RangeOriginSwitch">RangeOriginSwitch</a>: <i>String</i>
    <a href="#servicetype" title="ServiceType">ServiceType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#httpsconfig" title="HttpsConfig">HttpsConfig</a>: <i>
      - <a href="httpsconfigdefinition.md">HttpsConfigDefinition</a></i>
    <a href="#origin" title="Origin">Origin</a>: <i>
      - <a href="origindefinition.md">OriginDefinition</a></i>
    <a href="#requestheader" title="RequestHeader">RequestHeader</a>: <i>
      - <a href="requestheaderdefinition.md">RequestHeaderDefinition</a></i>
    <a href="#rulecache" title="RuleCache">RuleCache</a>: <i>
      - <a href="rulecachedefinition.md">RuleCacheDefinition</a></i>
</pre>

## Properties

#### Area

Domain name acceleration region. `mainland`: acceleration inside mainland China, `overseas`: acceleration outside mainland China, `global`: global acceleration. Overseas acceleration service must be enabled to use overseas acceleration and global acceleration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Name of the acceleration domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullUrlCache

Whether to enable full-path cache. Default value is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The project CDN belongs to, default to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RangeOriginSwitch

Sharding back to source configuration switch. Valid values are `on` and `off`. Default value is `on`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceType

Acceleration domain name service type. `web`: static acceleration, `download`: download acceleration, `media`: streaming media VOD acceleration.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Tags of cdn domain.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpsConfig

_Required_: No

_Type_: List of <a href="httpsconfigdefinition.md">HttpsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

_Required_: No

_Type_: List of <a href="origindefinition.md">OriginDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestHeader

_Required_: No

_Type_: List of <a href="requestheaderdefinition.md">RequestHeaderDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleCache

_Required_: No

_Type_: List of <a href="rulecachedefinition.md">RuleCacheDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Cname

Returns the <code>Cname</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

