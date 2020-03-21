# Terraform::OCI::WaasWaasPolicy CachingRules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#cachingduration" title="CachingDuration">CachingDuration</a>" : <i>String</i>,
    "<a href="#clientcachingduration" title="ClientCachingDuration">ClientCachingDuration</a>" : <i>String</i>,
    "<a href="#isclientcachingenabled" title="IsClientCachingEnabled">IsClientCachingEnabled</a>" : <i>Boolean</i>,
    "<a href="#key" title="Key">Key</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#criteria" title="Criteria">Criteria</a>" : <i>[ <a href="cachingrules-criteria.md">Criteria</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#cachingduration" title="CachingDuration">CachingDuration</a>: <i>String</i>
<a href="#clientcachingduration" title="ClientCachingDuration">ClientCachingDuration</a>: <i>String</i>
<a href="#isclientcachingenabled" title="IsClientCachingEnabled">IsClientCachingEnabled</a>: <i>Boolean</i>
<a href="#key" title="Key">Key</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#criteria" title="Criteria">Criteria</a>: <i>
      - <a href="cachingrules-criteria.md">Criteria</a></i>
</pre>

## Properties

#### Action

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CachingDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCachingDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsClientCachingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Criteria

_Required_: No

_Type_: List of <a href="cachingrules-criteria.md">Criteria</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

