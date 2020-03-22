# Terraform::AWS::PinpointApp

CloudFormation equivalent of aws_pinpoint_app

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::PinpointApp",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#campaignhook" title="CampaignHook">CampaignHook</a>" : <i>[ <a href="campaignhook.md">CampaignHook</a>, ... ]</i>,
        "<a href="#limits" title="Limits">Limits</a>" : <i>[ <a href="limits.md">Limits</a>, ... ]</i>,
        "<a href="#quiettime" title="QuietTime">QuietTime</a>" : <i>[ <a href="quiettime.md">QuietTime</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::PinpointApp
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#campaignhook" title="CampaignHook">CampaignHook</a>: <i>
      - <a href="campaignhook.md">CampaignHook</a></i>
    <a href="#limits" title="Limits">Limits</a>: <i>
      - <a href="limits.md">Limits</a></i>
    <a href="#quiettime" title="QuietTime">QuietTime</a>: <i>
      - <a href="quiettime.md">QuietTime</a></i>
</pre>

## Properties

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CampaignHook

_Required_: No

_Type_: List of <a href="campaignhook.md">CampaignHook</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limits

_Required_: No

_Type_: List of <a href="limits.md">Limits</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuietTime

_Required_: No

_Type_: List of <a href="quiettime.md">QuietTime</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApplicationId

Returns the <code>ApplicationId</code> value.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

