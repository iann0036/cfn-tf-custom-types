# TF::GoogleBeta::GoogleDataprocMetastoreService HiveMetastoreConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configoverrides" title="ConfigOverrides">ConfigOverrides</a>" : <i>[ <a href="configoverridesdefinition.md">ConfigOverridesDefinition</a>, ... ]</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#kerberosconfig" title="KerberosConfig">KerberosConfig</a>" : <i>[ <a href="kerberosconfigdefinition.md">KerberosConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configoverrides" title="ConfigOverrides">ConfigOverrides</a>: <i>
      - <a href="configoverridesdefinition.md">ConfigOverridesDefinition</a></i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#kerberosconfig" title="KerberosConfig">KerberosConfig</a>: <i>
      - <a href="kerberosconfigdefinition.md">KerberosConfigDefinition</a></i>
</pre>

## Properties

#### ConfigOverrides

_Required_: No

_Type_: List of <a href="configoverridesdefinition.md">ConfigOverridesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KerberosConfig

_Required_: No

_Type_: List of <a href="kerberosconfigdefinition.md">KerberosConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

