# Terraform::AzureRM::ApiManagement SignUp TermsOfService

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#consentrequired" title="ConsentRequired">ConsentRequired</a>" : <i>Boolean</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#text" title="Text">Text</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#consentrequired" title="ConsentRequired">ConsentRequired</a>: <i>Boolean</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#text" title="Text">Text</a>: <i>String</i>
</pre>

## Properties

#### ConsentRequired

Should the user be asked for consent during sign up?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Should Terms of Service be displayed during sign up?.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Text

The Terms of Service which users are required to agree to in order to sign up.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

