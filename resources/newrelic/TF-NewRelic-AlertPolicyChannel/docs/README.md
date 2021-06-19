# TF::NewRelic::AlertPolicyChannel

Use this resource to map alert policies to alert channels in New Relic.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::AlertPolicyChannel",
    "Properties" : {
        "<a href="#channelids" title="ChannelIds">ChannelIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::AlertPolicyChannel
Properties:
    <a href="#channelids" title="ChannelIds">ChannelIds</a>: <i>
      - Double</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>Double</i>
</pre>

## Properties

#### ChannelIds

Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift your Terraform state.

_Required_: Yes

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

The ID of the policy.
- `channel_ids` - (Required) Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to avoid drift your Terraform state.

_Required_: Yes

_Type_: Double

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

