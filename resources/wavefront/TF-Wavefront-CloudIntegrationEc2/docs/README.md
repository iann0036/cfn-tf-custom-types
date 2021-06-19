# TF::Wavefront::CloudIntegrationEc2

CloudFormation equivalent of wavefront_cloud_integration_ec2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Wavefront::CloudIntegrationEc2",
    "Properties" : {
        "<a href="#additionaltags" title="AdditionalTags">AdditionalTags</a>" : <i>[ <a href="additionaltagsdefinition.md">AdditionalTagsDefinition</a>, ... ]</i>,
        "<a href="#externalid" title="ExternalId">ExternalId</a>" : <i>String</i>,
        "<a href="#forcesave" title="ForceSave">ForceSave</a>" : <i>Boolean</i>,
        "<a href="#hostnametags" title="HostnameTags">HostnameTags</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#servicerefreshrateinminutes" title="ServiceRefreshRateInMinutes">ServiceRefreshRateInMinutes</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Wavefront::CloudIntegrationEc2
Properties:
    <a href="#additionaltags" title="AdditionalTags">AdditionalTags</a>: <i>
      - <a href="additionaltagsdefinition.md">AdditionalTagsDefinition</a></i>
    <a href="#externalid" title="ExternalId">ExternalId</a>: <i>String</i>
    <a href="#forcesave" title="ForceSave">ForceSave</a>: <i>Boolean</i>
    <a href="#hostnametags" title="HostnameTags">HostnameTags</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#servicerefreshrateinminutes" title="ServiceRefreshRateInMinutes">ServiceRefreshRateInMinutes</a>: <i>Double</i>
</pre>

## Properties

#### AdditionalTags

_Required_: No

_Type_: List of <a href="additionaltagsdefinition.md">AdditionalTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceSave

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

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

