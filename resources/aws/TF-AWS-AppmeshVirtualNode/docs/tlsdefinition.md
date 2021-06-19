# TF::AWS::AppmeshVirtualNode TlsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enforce" title="Enforce">Enforce</a>" : <i>Boolean</i>,
    "<a href="#ports" title="Ports">Ports</a>" : <i>[ Double, ... ]</i>,
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ <a href="certificatedefinition.md">CertificateDefinition</a>, ... ]</i>,
    "<a href="#validation" title="Validation">Validation</a>" : <i>[ <a href="validationdefinition.md">ValidationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enforce" title="Enforce">Enforce</a>: <i>Boolean</i>
<a href="#ports" title="Ports">Ports</a>: <i>
      - Double</i>
<a href="#certificate" title="Certificate">Certificate</a>: <i>
      - <a href="certificatedefinition.md">CertificateDefinition</a></i>
<a href="#validation" title="Validation">Validation</a>: <i>
      - <a href="validationdefinition.md">ValidationDefinition</a></i>
</pre>

## Properties

#### Enforce

Whether the policy is enforced. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

One or more ports that the policy is enforced for.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: List of <a href="certificatedefinition.md">CertificateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Validation

_Required_: No

_Type_: List of <a href="validationdefinition.md">ValidationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

