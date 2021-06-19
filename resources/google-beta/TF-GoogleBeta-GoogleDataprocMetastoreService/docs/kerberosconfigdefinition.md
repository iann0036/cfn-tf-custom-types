# TF::GoogleBeta::GoogleDataprocMetastoreService KerberosConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#krb5configgcsuri" title="Krb5ConfigGcsUri">Krb5ConfigGcsUri</a>" : <i>String</i>,
    "<a href="#principal" title="Principal">Principal</a>" : <i>String</i>,
    "<a href="#keytab" title="Keytab">Keytab</a>" : <i>[ <a href="keytabdefinition.md">KeytabDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#krb5configgcsuri" title="Krb5ConfigGcsUri">Krb5ConfigGcsUri</a>: <i>String</i>
<a href="#principal" title="Principal">Principal</a>: <i>String</i>
<a href="#keytab" title="Keytab">Keytab</a>: <i>
      - <a href="keytabdefinition.md">KeytabDefinition</a></i>
</pre>

## Properties

#### Krb5ConfigGcsUri

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Principal

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keytab

_Required_: No

_Type_: List of <a href="keytabdefinition.md">KeytabDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

