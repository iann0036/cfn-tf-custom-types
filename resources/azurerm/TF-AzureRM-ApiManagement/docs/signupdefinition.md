# TF::AzureRM::ApiManagement SignUpDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#termsofservice" title="TermsOfService">TermsOfService</a>" : <i>[ <a href="termsofservicedefinition.md">TermsOfServiceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#termsofservice" title="TermsOfService">TermsOfService</a>: <i>
      - <a href="termsofservicedefinition.md">TermsOfServiceDefinition</a></i>
</pre>

## Properties

#### Enabled

Can users sign up on the development portal?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TermsOfService

_Required_: No

_Type_: List of <a href="termsofservicedefinition.md">TermsOfServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

