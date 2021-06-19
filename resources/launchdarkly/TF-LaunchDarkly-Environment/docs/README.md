# TF::LaunchDarkly::Environment

Provides a LaunchDarkly environment resource.

This resource allows you to create and manage environments in your LaunchDarkly organization.

-> **Note:** Mixing the use of nested `environments` blocks in the [`launchdarkly_project`](/docs/providers/launchdarkly/r/project.html) resource and `launchdarkly_environment` resources is not recommended.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::LaunchDarkly::Environment",
    "Properties" : {
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#confirmchanges" title="ConfirmChanges">ConfirmChanges</a>" : <i>Boolean</i>,
        "<a href="#defaulttrackevents" title="DefaultTrackEvents">DefaultTrackEvents</a>" : <i>Boolean</i>,
        "<a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>" : <i>Double</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectkey" title="ProjectKey">ProjectKey</a>" : <i>String</i>,
        "<a href="#requirecomments" title="RequireComments">RequireComments</a>" : <i>Boolean</i>,
        "<a href="#securemode" title="SecureMode">SecureMode</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::LaunchDarkly::Environment
Properties:
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#confirmchanges" title="ConfirmChanges">ConfirmChanges</a>: <i>Boolean</i>
    <a href="#defaulttrackevents" title="DefaultTrackEvents">DefaultTrackEvents</a>: <i>Boolean</i>
    <a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>: <i>Double</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectkey" title="ProjectKey">ProjectKey</a>: <i>String</i>
    <a href="#requirecomments" title="RequireComments">RequireComments</a>: <i>Boolean</i>
    <a href="#securemode" title="SecureMode">SecureMode</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
</pre>

## Properties

#### Color

The color swatch as an RGB hex value with no leading `#`. For example: `000000`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfirmChanges

Set to `true` if this environment requires confirmation for flag and segment changes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTrackEvents

Set to `true` to enable data export for every flag created in this environment after you configure this argument. To learn more, read [Data Export](https://docs.launchdarkly.com/docs/data-export).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTtl

The TTL for the environment. This must be between 0 and 60 minutes. The TTL setting only applies to environments using the PHP SDK. To learn more, read [TTL settings](https://docs.launchdarkly.com/docs/environments#section-ttl-settings).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

The project-unique key for the environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectKey

- The environment's project key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireComments

Set to `true` if this environment requires comments for flag and segment changes.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureMode

Set to `true` to ensure a user of the client-side SDK cannot impersonate another user.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Set of tags associated with the environment.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApiKey

Returns the <code>ApiKey</code> value.

#### ClientSideId

Returns the <code>ClientSideId</code> value.

#### Id

Returns the <code>Id</code> value.

#### MobileKey

Returns the <code>MobileKey</code> value.

