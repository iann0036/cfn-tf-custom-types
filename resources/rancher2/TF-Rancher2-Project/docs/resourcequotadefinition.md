# TF::Rancher2::Project ResourceQuotaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#namespacedefaultlimit" title="NamespaceDefaultLimit">NamespaceDefaultLimit</a>" : <i>[ <a href="namespacedefaultlimitdefinition.md">NamespaceDefaultLimitDefinition</a>, ... ]</i>,
    "<a href="#projectlimit" title="ProjectLimit">ProjectLimit</a>" : <i>[ <a href="projectlimitdefinition.md">ProjectLimitDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#namespacedefaultlimit" title="NamespaceDefaultLimit">NamespaceDefaultLimit</a>: <i>
      - <a href="namespacedefaultlimitdefinition.md">NamespaceDefaultLimitDefinition</a></i>
<a href="#projectlimit" title="ProjectLimit">ProjectLimit</a>: <i>
      - <a href="projectlimitdefinition.md">ProjectLimitDefinition</a></i>
</pre>

## Properties

#### NamespaceDefaultLimit

_Required_: No

_Type_: List of <a href="namespacedefaultlimitdefinition.md">NamespaceDefaultLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectLimit

_Required_: No

_Type_: List of <a href="projectlimitdefinition.md">ProjectLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

