# TF::TencentCloud::CdnDomain RuleCacheDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cachetime" title="CacheTime">CacheTime</a>" : <i>Double</i>,
    "<a href="#comparemaxage" title="CompareMaxAge">CompareMaxAge</a>" : <i>String</i>,
    "<a href="#followoriginswitch" title="FollowOriginSwitch">FollowOriginSwitch</a>" : <i>String</i>,
    "<a href="#ignorecachecontrol" title="IgnoreCacheControl">IgnoreCacheControl</a>" : <i>String</i>,
    "<a href="#ignoresetcookie" title="IgnoreSetCookie">IgnoreSetCookie</a>" : <i>String</i>,
    "<a href="#nocacheswitch" title="NoCacheSwitch">NoCacheSwitch</a>" : <i>String</i>,
    "<a href="#revalidate" title="ReValidate">ReValidate</a>" : <i>String</i>,
    "<a href="#rulepaths" title="RulePaths">RulePaths</a>" : <i>[ String, ... ]</i>,
    "<a href="#ruletype" title="RuleType">RuleType</a>" : <i>String</i>,
    "<a href="#switch" title="Switch">Switch</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#cachetime" title="CacheTime">CacheTime</a>: <i>Double</i>
<a href="#comparemaxage" title="CompareMaxAge">CompareMaxAge</a>: <i>String</i>
<a href="#followoriginswitch" title="FollowOriginSwitch">FollowOriginSwitch</a>: <i>String</i>
<a href="#ignorecachecontrol" title="IgnoreCacheControl">IgnoreCacheControl</a>: <i>String</i>
<a href="#ignoresetcookie" title="IgnoreSetCookie">IgnoreSetCookie</a>: <i>String</i>
<a href="#nocacheswitch" title="NoCacheSwitch">NoCacheSwitch</a>: <i>String</i>
<a href="#revalidate" title="ReValidate">ReValidate</a>: <i>String</i>
<a href="#rulepaths" title="RulePaths">RulePaths</a>: <i>
      - String</i>
<a href="#ruletype" title="RuleType">RuleType</a>: <i>String</i>
<a href="#switch" title="Switch">Switch</a>: <i>String</i>
</pre>

## Properties

#### CacheTime

Cache expiration time setting, the unit is second, the maximum can be set to 365 days.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CompareMaxAge

Advanced cache expiration configuration. When it is turned on, it will compare the max-age value returned by the origin site with the cache expiration time set in CacheRules, and take the minimum value to cache at the node. Valid values are `on` and `off`. Default value is `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowOriginSwitch

Follow the source station configuration switch. Valid values are `on` and `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreCacheControl

Force caching. After opening, the no-store and no-cache resources returned by the origin site will also be cached in accordance with the CacheRules rules. Valid values are `on` and `off`. Default value is `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreSetCookie

Ignore the Set-Cookie header of the origin site. Valid values are `on` and `off`. Default value is `off`. This parameter is for white-list customer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoCacheSwitch

Cache configuration switch. Valid values are `on` and `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReValidate

Always check back to origin. Valid values are `on` and `off`. Default value is `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulePaths

Matching content under the corresponding type of CacheType: `all`: fill *, `file`: fill in the suffix name, such as jpg, txt, `directory`: fill in the path, such as /xxx/test, `path`: fill in the absolute path, such as /xxx/test.html, `index`: fill /, `default`: Fill `no max-age`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleType

Rule type. The following types are supported: `all`: all documents take effect, `file`: the specified file suffix takes effect, `directory`: the specified path takes effect, `path`: specify the absolute path to take effect, `index`: home page, `default`: effective when the source site has no max-age.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Switch

Cache configuration switch. Valid values are `on` and `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

