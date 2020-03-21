# Terraform::AWS::AthenaWorkgroup ResultConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#outputlocation" title="OutputLocation">OutputLocation</a>" : <i>String</i>,
    "<a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>" : <i>[ <a href="resultconfiguration-encryptionconfiguration.md">EncryptionConfiguration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#outputlocation" title="OutputLocation">OutputLocation</a>: <i>String</i>
<a href="#encryptionconfiguration" title="EncryptionConfiguration">EncryptionConfiguration</a>: <i>
      - <a href="resultconfiguration-encryptionconfiguration.md">EncryptionConfiguration</a></i>
</pre>

## Properties

#### OutputLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfiguration

_Required_: No

_Type_: List of <a href="resultconfiguration-encryptionconfiguration.md">EncryptionConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

