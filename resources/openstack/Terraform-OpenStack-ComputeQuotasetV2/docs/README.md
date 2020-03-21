# Terraform::OpenStack::ComputeQuotasetV2

Manages a V2 compute quotaset resource within OpenStack.

~> **Note:** This usually requires admin privileges.

~> **Note:** This resource has a no-op deletion so no actual actions will be done against the OpenStack API 
    in case of delete call.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::ComputeQuotasetV2",
    "Properties" : {
        "<a href="#cores" title="Cores">Cores</a>" : <i>Double</i>,
        "<a href="#fixedips" title="FixedIps">FixedIps</a>" : <i>Double</i>,
        "<a href="#floatingips" title="FloatingIps">FloatingIps</a>" : <i>Double</i>,
        "<a href="#injectedfilecontentbytes" title="InjectedFileContentBytes">InjectedFileContentBytes</a>" : <i>Double</i>,
        "<a href="#injectedfilepathbytes" title="InjectedFilePathBytes">InjectedFilePathBytes</a>" : <i>Double</i>,
        "<a href="#injectedfiles" title="InjectedFiles">InjectedFiles</a>" : <i>Double</i>,
        "<a href="#instances" title="Instances">Instances</a>" : <i>Double</i>,
        "<a href="#keypairs" title="KeyPairs">KeyPairs</a>" : <i>Double</i>,
        "<a href="#metadataitems" title="MetadataItems">MetadataItems</a>" : <i>Double</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#ram" title="Ram">Ram</a>" : <i>Double</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#securitygrouprules" title="SecurityGroupRules">SecurityGroupRules</a>" : <i>Double</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>Double</i>,
        "<a href="#servergroupmembers" title="ServerGroupMembers">ServerGroupMembers</a>" : <i>Double</i>,
        "<a href="#servergroups" title="ServerGroups">ServerGroups</a>" : <i>Double</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::ComputeQuotasetV2
Properties:
    <a href="#cores" title="Cores">Cores</a>: <i>Double</i>
    <a href="#fixedips" title="FixedIps">FixedIps</a>: <i>Double</i>
    <a href="#floatingips" title="FloatingIps">FloatingIps</a>: <i>Double</i>
    <a href="#injectedfilecontentbytes" title="InjectedFileContentBytes">InjectedFileContentBytes</a>: <i>Double</i>
    <a href="#injectedfilepathbytes" title="InjectedFilePathBytes">InjectedFilePathBytes</a>: <i>Double</i>
    <a href="#injectedfiles" title="InjectedFiles">InjectedFiles</a>: <i>Double</i>
    <a href="#instances" title="Instances">Instances</a>: <i>Double</i>
    <a href="#keypairs" title="KeyPairs">KeyPairs</a>: <i>Double</i>
    <a href="#metadataitems" title="MetadataItems">MetadataItems</a>: <i>Double</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#ram" title="Ram">Ram</a>: <i>Double</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#securitygrouprules" title="SecurityGroupRules">SecurityGroupRules</a>: <i>Double</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>Double</i>
    <a href="#servergroupmembers" title="ServerGroupMembers">ServerGroupMembers</a>: <i>Double</i>
    <a href="#servergroups" title="ServerGroups">ServerGroups</a>: <i>Double</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Cores

Quota value for cores.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FixedIps

Quota value for fixed IPs.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FloatingIps

Quota value for floating IPs.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InjectedFileContentBytes

Quota value for content bytes
of injected files. Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InjectedFilePathBytes

Quota value for path bytes of
injected files. Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InjectedFiles

Quota value for injected files.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

Quota value for instances.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPairs

Quota value for key pairs.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetadataItems

Quota value for metadata items.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

ID of the project to manage quotas.
Changing this creates a new quotaset.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ram

Quota value for RAM.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to create the volume. If
omitted, the `region` argument of the provider is used. Changing this
creates a new quotaset.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupRules

Quota value for security group rules.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

Quota value for security groups.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerGroupMembers

Quota value for server groups members.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerGroups

Quota value for server groups.
Changing this updates the existing quotaset.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

