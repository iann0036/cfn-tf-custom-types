# TF::Rancher2::CloudCredential

CloudFormation equivalent of rancher2_cloud_credential

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::CloudCredential",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#amazonec2credentialconfig" title="Amazonec2CredentialConfig">Amazonec2CredentialConfig</a>" : <i>[ <a href="amazonec2credentialconfigdefinition.md">Amazonec2CredentialConfigDefinition</a>, ... ]</i>,
        "<a href="#azurecredentialconfig" title="AzureCredentialConfig">AzureCredentialConfig</a>" : <i>[ <a href="azurecredentialconfigdefinition.md">AzureCredentialConfigDefinition</a>, ... ]</i>,
        "<a href="#digitaloceancredentialconfig" title="DigitaloceanCredentialConfig">DigitaloceanCredentialConfig</a>" : <i>[ <a href="digitaloceancredentialconfigdefinition.md">DigitaloceanCredentialConfigDefinition</a>, ... ]</i>,
        "<a href="#googlecredentialconfig" title="GoogleCredentialConfig">GoogleCredentialConfig</a>" : <i>[ <a href="googlecredentialconfigdefinition.md">GoogleCredentialConfigDefinition</a>, ... ]</i>,
        "<a href="#linodecredentialconfig" title="LinodeCredentialConfig">LinodeCredentialConfig</a>" : <i>[ <a href="linodecredentialconfigdefinition.md">LinodeCredentialConfigDefinition</a>, ... ]</i>,
        "<a href="#openstackcredentialconfig" title="OpenstackCredentialConfig">OpenstackCredentialConfig</a>" : <i>[ <a href="openstackcredentialconfigdefinition.md">OpenstackCredentialConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#vspherecredentialconfig" title="VsphereCredentialConfig">VsphereCredentialConfig</a>" : <i>[ <a href="vspherecredentialconfigdefinition.md">VsphereCredentialConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::CloudCredential
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#amazonec2credentialconfig" title="Amazonec2CredentialConfig">Amazonec2CredentialConfig</a>: <i>
      - <a href="amazonec2credentialconfigdefinition.md">Amazonec2CredentialConfigDefinition</a></i>
    <a href="#azurecredentialconfig" title="AzureCredentialConfig">AzureCredentialConfig</a>: <i>
      - <a href="azurecredentialconfigdefinition.md">AzureCredentialConfigDefinition</a></i>
    <a href="#digitaloceancredentialconfig" title="DigitaloceanCredentialConfig">DigitaloceanCredentialConfig</a>: <i>
      - <a href="digitaloceancredentialconfigdefinition.md">DigitaloceanCredentialConfigDefinition</a></i>
    <a href="#googlecredentialconfig" title="GoogleCredentialConfig">GoogleCredentialConfig</a>: <i>
      - <a href="googlecredentialconfigdefinition.md">GoogleCredentialConfigDefinition</a></i>
    <a href="#linodecredentialconfig" title="LinodeCredentialConfig">LinodeCredentialConfig</a>: <i>
      - <a href="linodecredentialconfigdefinition.md">LinodeCredentialConfigDefinition</a></i>
    <a href="#openstackcredentialconfig" title="OpenstackCredentialConfig">OpenstackCredentialConfig</a>: <i>
      - <a href="openstackcredentialconfigdefinition.md">OpenstackCredentialConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#vspherecredentialconfig" title="VsphereCredentialConfig">VsphereCredentialConfig</a>: <i>
      - <a href="vspherecredentialconfigdefinition.md">VsphereCredentialConfigDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Amazonec2CredentialConfig

_Required_: No

_Type_: List of <a href="amazonec2credentialconfigdefinition.md">Amazonec2CredentialConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureCredentialConfig

_Required_: No

_Type_: List of <a href="azurecredentialconfigdefinition.md">AzureCredentialConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DigitaloceanCredentialConfig

_Required_: No

_Type_: List of <a href="digitaloceancredentialconfigdefinition.md">DigitaloceanCredentialConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GoogleCredentialConfig

_Required_: No

_Type_: List of <a href="googlecredentialconfigdefinition.md">GoogleCredentialConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinodeCredentialConfig

_Required_: No

_Type_: List of <a href="linodecredentialconfigdefinition.md">LinodeCredentialConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenstackCredentialConfig

_Required_: No

_Type_: List of <a href="openstackcredentialconfigdefinition.md">OpenstackCredentialConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsphereCredentialConfig

_Required_: No

_Type_: List of <a href="vspherecredentialconfigdefinition.md">VsphereCredentialConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Driver

Returns the <code>Driver</code> value.

#### Id

Returns the <code>Id</code> value.

