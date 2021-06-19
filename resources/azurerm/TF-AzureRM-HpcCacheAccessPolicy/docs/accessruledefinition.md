# TF::AzureRM::HpcCacheAccessPolicy AccessRuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#access" title="Access">Access</a>" : <i>String</i>,
    "<a href="#anonymousgid" title="AnonymousGid">AnonymousGid</a>" : <i>Double</i>,
    "<a href="#anonymousuid" title="AnonymousUid">AnonymousUid</a>" : <i>Double</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
    "<a href="#rootsquashenabled" title="RootSquashEnabled">RootSquashEnabled</a>" : <i>Boolean</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
    "<a href="#submountaccessenabled" title="SubmountAccessEnabled">SubmountAccessEnabled</a>" : <i>Boolean</i>,
    "<a href="#suidenabled" title="SuidEnabled">SuidEnabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#access" title="Access">Access</a>: <i>String</i>
<a href="#anonymousgid" title="AnonymousGid">AnonymousGid</a>: <i>Double</i>
<a href="#anonymousuid" title="AnonymousUid">AnonymousUid</a>: <i>Double</i>
<a href="#filter" title="Filter">Filter</a>: <i>String</i>
<a href="#rootsquashenabled" title="RootSquashEnabled">RootSquashEnabled</a>: <i>Boolean</i>
<a href="#scope" title="Scope">Scope</a>: <i>String</i>
<a href="#submountaccessenabled" title="SubmountAccessEnabled">SubmountAccessEnabled</a>: <i>Boolean</i>
<a href="#suidenabled" title="SuidEnabled">SuidEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### Access

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnonymousGid

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnonymousUid

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootSquashEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubmountAccessEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuidEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

