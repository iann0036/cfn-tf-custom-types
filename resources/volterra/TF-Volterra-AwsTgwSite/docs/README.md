# TF::Volterra::AwsTgwSite

CloudFormation equivalent of volterra_aws_tgw_site

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::AwsTgwSite",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#logsstreamingdisabled" title="LogsStreamingDisabled">LogsStreamingDisabled</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#awsparameters" title="AwsParameters">AwsParameters</a>" : <i>[ <a href="awsparametersdefinition.md">AwsParametersDefinition</a>, ... ]</i>,
        "<a href="#coordinates" title="Coordinates">Coordinates</a>" : <i>[ <a href="coordinatesdefinition.md">CoordinatesDefinition</a>, ... ]</i>,
        "<a href="#logreceiver" title="LogReceiver">LogReceiver</a>" : <i>[ <a href="logreceiverdefinition.md">LogReceiverDefinition</a>, ... ]</i>,
        "<a href="#os" title="Os">Os</a>" : <i>[ <a href="osdefinition.md">OsDefinition</a>, ... ]</i>,
        "<a href="#sw" title="Sw">Sw</a>" : <i>[ <a href="swdefinition.md">SwDefinition</a>, ... ]</i>,
        "<a href="#tgwsecurity" title="TgwSecurity">TgwSecurity</a>" : <i>[ <a href="tgwsecuritydefinition.md">TgwSecurityDefinition</a>, ... ]</i>,
        "<a href="#vnconfig" title="VnConfig">VnConfig</a>" : <i>[ <a href="vnconfigdefinition.md">VnConfigDefinition</a>, ... ]</i>,
        "<a href="#vpcattachments" title="VpcAttachments">VpcAttachments</a>" : <i>[ <a href="vpcattachmentsdefinition.md">VpcAttachmentsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::AwsTgwSite
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#logsstreamingdisabled" title="LogsStreamingDisabled">LogsStreamingDisabled</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#awsparameters" title="AwsParameters">AwsParameters</a>: <i>
      - <a href="awsparametersdefinition.md">AwsParametersDefinition</a></i>
    <a href="#coordinates" title="Coordinates">Coordinates</a>: <i>
      - <a href="coordinatesdefinition.md">CoordinatesDefinition</a></i>
    <a href="#logreceiver" title="LogReceiver">LogReceiver</a>: <i>
      - <a href="logreceiverdefinition.md">LogReceiverDefinition</a></i>
    <a href="#os" title="Os">Os</a>: <i>
      - <a href="osdefinition.md">OsDefinition</a></i>
    <a href="#sw" title="Sw">Sw</a>: <i>
      - <a href="swdefinition.md">SwDefinition</a></i>
    <a href="#tgwsecurity" title="TgwSecurity">TgwSecurity</a>: <i>
      - <a href="tgwsecuritydefinition.md">TgwSecurityDefinition</a></i>
    <a href="#vnconfig" title="VnConfig">VnConfig</a>: <i>
      - <a href="vnconfigdefinition.md">VnConfigDefinition</a></i>
    <a href="#vpcattachments" title="VpcAttachments">VpcAttachments</a>: <i>
      - <a href="vpcattachmentsdefinition.md">VpcAttachmentsDefinition</a></i>
</pre>

## Properties

#### Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogsStreamingDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsParameters

_Required_: No

_Type_: List of <a href="awsparametersdefinition.md">AwsParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Coordinates

_Required_: No

_Type_: List of <a href="coordinatesdefinition.md">CoordinatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogReceiver

_Required_: No

_Type_: List of <a href="logreceiverdefinition.md">LogReceiverDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Os

_Required_: No

_Type_: List of <a href="osdefinition.md">OsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sw

_Required_: No

_Type_: List of <a href="swdefinition.md">SwDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgwSecurity

_Required_: No

_Type_: List of <a href="tgwsecuritydefinition.md">TgwSecurityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VnConfig

_Required_: No

_Type_: List of <a href="vnconfigdefinition.md">VnConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcAttachments

_Required_: No

_Type_: List of <a href="vpcattachmentsdefinition.md">VpcAttachmentsDefinition</a>

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

