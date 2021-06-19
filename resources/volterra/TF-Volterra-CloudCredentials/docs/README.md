# TF::Volterra::CloudCredentials

CloudFormation equivalent of volterra_cloud_credentials

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::CloudCredentials",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#awssecretkey" title="AwsSecretKey">AwsSecretKey</a>" : <i>[ <a href="awssecretkeydefinition.md">AwsSecretKeyDefinition</a>, ... ]</i>,
        "<a href="#azureclientsecret" title="AzureClientSecret">AzureClientSecret</a>" : <i>[ <a href="azureclientsecretdefinition.md">AzureClientSecretDefinition</a>, ... ]</i>,
        "<a href="#azurepfxcertificate" title="AzurePfxCertificate">AzurePfxCertificate</a>" : <i>[ <a href="azurepfxcertificatedefinition.md">AzurePfxCertificateDefinition</a>, ... ]</i>,
        "<a href="#gcpcredfile" title="GcpCredFile">GcpCredFile</a>" : <i>[ <a href="gcpcredfiledefinition.md">GcpCredFileDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::CloudCredentials
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#awssecretkey" title="AwsSecretKey">AwsSecretKey</a>: <i>
      - <a href="awssecretkeydefinition.md">AwsSecretKeyDefinition</a></i>
    <a href="#azureclientsecret" title="AzureClientSecret">AzureClientSecret</a>: <i>
      - <a href="azureclientsecretdefinition.md">AzureClientSecretDefinition</a></i>
    <a href="#azurepfxcertificate" title="AzurePfxCertificate">AzurePfxCertificate</a>: <i>
      - <a href="azurepfxcertificatedefinition.md">AzurePfxCertificateDefinition</a></i>
    <a href="#gcpcredfile" title="GcpCredFile">GcpCredFile</a>: <i>
      - <a href="gcpcredfiledefinition.md">GcpCredFileDefinition</a></i>
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

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsSecretKey

_Required_: No

_Type_: List of <a href="awssecretkeydefinition.md">AwsSecretKeyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureClientSecret

_Required_: No

_Type_: List of <a href="azureclientsecretdefinition.md">AzureClientSecretDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzurePfxCertificate

_Required_: No

_Type_: List of <a href="azurepfxcertificatedefinition.md">AzurePfxCertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcpCredFile

_Required_: No

_Type_: List of <a href="gcpcredfiledefinition.md">GcpCredFileDefinition</a>

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

