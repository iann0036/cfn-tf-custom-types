# TF::OpenNebula::Group QuotasDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#datastorequotas" title="DatastoreQuotas">DatastoreQuotas</a>" : <i>[ <a href="datastorequotasdefinition.md">DatastoreQuotasDefinition</a>, ... ]</i>,
    "<a href="#imagequotas" title="ImageQuotas">ImageQuotas</a>" : <i>[ <a href="imagequotasdefinition.md">ImageQuotasDefinition</a>, ... ]</i>,
    "<a href="#networkquotas" title="NetworkQuotas">NetworkQuotas</a>" : <i>[ <a href="networkquotasdefinition.md">NetworkQuotasDefinition</a>, ... ]</i>,
    "<a href="#vmquotas" title="VmQuotas">VmQuotas</a>" : <i>[ <a href="vmquotasdefinition.md">VmQuotasDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#datastorequotas" title="DatastoreQuotas">DatastoreQuotas</a>: <i>
      - <a href="datastorequotasdefinition.md">DatastoreQuotasDefinition</a></i>
<a href="#imagequotas" title="ImageQuotas">ImageQuotas</a>: <i>
      - <a href="imagequotasdefinition.md">ImageQuotasDefinition</a></i>
<a href="#networkquotas" title="NetworkQuotas">NetworkQuotas</a>: <i>
      - <a href="networkquotasdefinition.md">NetworkQuotasDefinition</a></i>
<a href="#vmquotas" title="VmQuotas">VmQuotas</a>: <i>
      - <a href="vmquotasdefinition.md">VmQuotasDefinition</a></i>
</pre>

## Properties

#### DatastoreQuotas

_Required_: No

_Type_: List of <a href="datastorequotasdefinition.md">DatastoreQuotasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageQuotas

_Required_: No

_Type_: List of <a href="imagequotasdefinition.md">ImageQuotasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkQuotas

_Required_: No

_Type_: List of <a href="networkquotasdefinition.md">NetworkQuotasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmQuotas

_Required_: No

_Type_: List of <a href="vmquotasdefinition.md">VmQuotasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

