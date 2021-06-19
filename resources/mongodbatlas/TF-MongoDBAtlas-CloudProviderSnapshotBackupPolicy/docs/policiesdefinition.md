# TF::MongoDBAtlas::CloudProviderSnapshotBackupPolicy PoliciesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#policyitem" title="PolicyItem">PolicyItem</a>" : <i>[ <a href="policyitemdefinition.md">PolicyItemDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#policyitem" title="PolicyItem">PolicyItem</a>: <i>
      - <a href="policyitemdefinition.md">PolicyItemDefinition</a></i>
</pre>

## Properties

#### Id

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyItem

_Required_: No

_Type_: List of <a href="policyitemdefinition.md">PolicyItemDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

