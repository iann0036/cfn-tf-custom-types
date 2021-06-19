# TF::Kubernetes::CertificateSigningRequest

Use this resource to generate TLS certificates using Kubernetes.

This is a *logical resource*, so it contributes only to the current Terraform state and does not persist any external managed resources.

This resource enables automation of [X.509](https://www.itu.int/rec/T-REC-X.509) credential provisioning (including TLS/SSL certificates). It does this by creating a CertificateSigningRequest using the Kubernetes API, which generates a certificate from the Certificate Authority (CA) configured in the Kubernetes cluster. The CSR can be approved automatically by Terraform, or it can be approved by a custom controller running in Kubernetes. See [Kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/) for all available options pertaining to CertificateSigningRequests.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Kubernetes::CertificateSigningRequest",
    "Properties" : {
        "<a href="#autoapprove" title="AutoApprove">AutoApprove</a>" : <i>Boolean</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ <a href="specdefinition.md">SpecDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Kubernetes::CertificateSigningRequest
Properties:
    <a href="#autoapprove" title="AutoApprove">AutoApprove</a>: <i>Boolean</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - <a href="specdefinition.md">SpecDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AutoApprove

Automatically approve the CertificateSigningRequest. Defaults to 'true'.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of <a href="specdefinition.md">SpecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Certificate

Returns the <code>Certificate</code> value.

#### Id

Returns the <code>Id</code> value.

