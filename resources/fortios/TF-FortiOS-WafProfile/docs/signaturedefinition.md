# TF::FortiOS::WafProfile SignatureDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#creditcarddetectionthreshold" title="CreditCardDetectionThreshold">CreditCardDetectionThreshold</a>" : <i>Double</i>,
    "<a href="#customsignature" title="CustomSignature">CustomSignature</a>" : <i>[ <a href="customsignaturedefinition.md">CustomSignatureDefinition</a>, ... ]</i>,
    "<a href="#disabledsignature" title="DisabledSignature">DisabledSignature</a>" : <i>[ <a href="disabledsignaturedefinition.md">DisabledSignatureDefinition</a>, ... ]</i>,
    "<a href="#disabledsubclass" title="DisabledSubClass">DisabledSubClass</a>" : <i>[ <a href="disabledsubclassdefinition.md">DisabledSubClassDefinition</a>, ... ]</i>,
    "<a href="#mainclass" title="MainClass">MainClass</a>" : <i>[ <a href="mainclassdefinition.md">MainClassDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#creditcarddetectionthreshold" title="CreditCardDetectionThreshold">CreditCardDetectionThreshold</a>: <i>Double</i>
<a href="#customsignature" title="CustomSignature">CustomSignature</a>: <i>
      - <a href="customsignaturedefinition.md">CustomSignatureDefinition</a></i>
<a href="#disabledsignature" title="DisabledSignature">DisabledSignature</a>: <i>
      - <a href="disabledsignaturedefinition.md">DisabledSignatureDefinition</a></i>
<a href="#disabledsubclass" title="DisabledSubClass">DisabledSubClass</a>: <i>
      - <a href="disabledsubclassdefinition.md">DisabledSubClassDefinition</a></i>
<a href="#mainclass" title="MainClass">MainClass</a>: <i>
      - <a href="mainclassdefinition.md">MainClassDefinition</a></i>
</pre>

## Properties

#### CreditCardDetectionThreshold

The minimum number of Credit cards to detect violation.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSignature

_Required_: No

_Type_: List of <a href="customsignaturedefinition.md">CustomSignatureDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisabledSignature

_Required_: No

_Type_: List of <a href="disabledsignaturedefinition.md">DisabledSignatureDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisabledSubClass

_Required_: No

_Type_: List of <a href="disabledsubclassdefinition.md">DisabledSubClassDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MainClass

_Required_: No

_Type_: List of <a href="mainclassdefinition.md">MainClassDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

