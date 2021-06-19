# TF::Wavefront::CloudIntegrationGcpBilling

CloudFormation equivalent of wavefront_cloud_integration_gcp_billing

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Wavefront::CloudIntegrationGcpBilling",
    "Properties" : {
        "<a href="#additionaltags" title="AdditionalTags">AdditionalTags</a>" : <i>[ <a href="additionaltagsdefinition.md">AdditionalTagsDefinition</a>, ... ]</i>,
        "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
        "<a href="#forcesave" title="ForceSave">ForceSave</a>" : <i>Boolean</i>,
        "<a href="#jsonkey" title="JsonKey">JsonKey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#servicerefreshrateinminutes" title="ServiceRefreshRateInMinutes">ServiceRefreshRateInMinutes</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Wavefront::CloudIntegrationGcpBilling
Properties:
    <a href="#additionaltags" title="AdditionalTags">AdditionalTags</a>: <i>
      - <a href="additionaltagsdefinition.md">AdditionalTagsDefinition</a></i>
    <a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
    <a href="#forcesave" title="ForceSave">ForceSave</a>: <i>Boolean</i>
    <a href="#jsonkey" title="JsonKey">JsonKey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#servicerefreshrateinminutes" title="ServiceRefreshRateInMinutes">ServiceRefreshRateInMinutes</a>: <i>Double</i>
</pre>

## Properties

#### AdditionalTags

_Required_: No

_Type_: List of <a href="additionaltagsdefinition.md">AdditionalTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApiKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceSave

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsonKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRefreshRateInMinutes

_Required_: No

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

