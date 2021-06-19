# TF::AWS::SignerSigningJob

Creates a Signer Signing Job.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SignerSigningJob",
    "Properties" : {
        "<a href="#ignoresigningjobfailure" title="IgnoreSigningJobFailure">IgnoreSigningJobFailure</a>" : <i>Boolean</i>,
        "<a href="#profilename" title="ProfileName">ProfileName</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destinationdefinition.md">DestinationDefinition</a>, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="sourcedefinition.md">SourceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SignerSigningJob
Properties:
    <a href="#ignoresigningjobfailure" title="IgnoreSigningJobFailure">IgnoreSigningJobFailure</a>: <i>Boolean</i>
    <a href="#profilename" title="ProfileName">ProfileName</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destinationdefinition.md">DestinationDefinition</a></i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="sourcedefinition.md">SourceDefinition</a></i>
</pre>

## Properties

#### IgnoreSigningJobFailure

Set this argument to `true` to ignore signing job failures and retrieve failed status and reason. Default `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileName

The name of the profile to initiate the signing operation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destinationdefinition.md">DestinationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="sourcedefinition.md">SourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CompletedAt

Returns the <code>CompletedAt</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### JobId

Returns the <code>JobId</code> value.

#### JobInvoker

Returns the <code>JobInvoker</code> value.

#### JobOwner

Returns the <code>JobOwner</code> value.

#### PlatformDisplayName

Returns the <code>PlatformDisplayName</code> value.

#### PlatformId

Returns the <code>PlatformId</code> value.

#### ProfileVersion

Returns the <code>ProfileVersion</code> value.

#### RequestedBy

Returns the <code>RequestedBy</code> value.

#### RevocationRecord

Returns the <code>RevocationRecord</code> value.

#### SignatureExpiresAt

Returns the <code>SignatureExpiresAt</code> value.

#### SignedObject

Returns the <code>SignedObject</code> value.

#### Status

Returns the <code>Status</code> value.

#### StatusReason

Returns the <code>StatusReason</code> value.

