# TF::GoogleBeta::GoogleDnsManagedZone

CloudFormation equivalent of google_dns_managed_zone

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleDnsManagedZone",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dnsname" title="DnsName">DnsName</a>" : <i>String</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#reverselookup" title="ReverseLookup">ReverseLookup</a>" : <i>Boolean</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#dnssecconfig" title="DnssecConfig">DnssecConfig</a>" : <i>[ <a href="dnssecconfigdefinition.md">DnssecConfigDefinition</a>, ... ]</i>,
        "<a href="#forwardingconfig" title="ForwardingConfig">ForwardingConfig</a>" : <i>[ <a href="forwardingconfigdefinition.md">ForwardingConfigDefinition</a>, ... ]</i>,
        "<a href="#peeringconfig" title="PeeringConfig">PeeringConfig</a>" : <i>[ <a href="peeringconfigdefinition.md">PeeringConfigDefinition</a>, ... ]</i>,
        "<a href="#privatevisibilityconfig" title="PrivateVisibilityConfig">PrivateVisibilityConfig</a>" : <i>[ <a href="privatevisibilityconfigdefinition.md">PrivateVisibilityConfigDefinition</a>, ... ]</i>,
        "<a href="#servicedirectoryconfig" title="ServiceDirectoryConfig">ServiceDirectoryConfig</a>" : <i>[ <a href="servicedirectoryconfigdefinition.md">ServiceDirectoryConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleDnsManagedZone
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dnsname" title="DnsName">DnsName</a>: <i>String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#reverselookup" title="ReverseLookup">ReverseLookup</a>: <i>Boolean</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#dnssecconfig" title="DnssecConfig">DnssecConfig</a>: <i>
      - <a href="dnssecconfigdefinition.md">DnssecConfigDefinition</a></i>
    <a href="#forwardingconfig" title="ForwardingConfig">ForwardingConfig</a>: <i>
      - <a href="forwardingconfigdefinition.md">ForwardingConfigDefinition</a></i>
    <a href="#peeringconfig" title="PeeringConfig">PeeringConfig</a>: <i>
      - <a href="peeringconfigdefinition.md">PeeringConfigDefinition</a></i>
    <a href="#privatevisibilityconfig" title="PrivateVisibilityConfig">PrivateVisibilityConfig</a>: <i>
      - <a href="privatevisibilityconfigdefinition.md">PrivateVisibilityConfigDefinition</a></i>
    <a href="#servicedirectoryconfig" title="ServiceDirectoryConfig">ServiceDirectoryConfig</a>: <i>
      - <a href="servicedirectoryconfigdefinition.md">ServiceDirectoryConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReverseLookup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnssecConfig

_Required_: No

_Type_: List of <a href="dnssecconfigdefinition.md">DnssecConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardingConfig

_Required_: No

_Type_: List of <a href="forwardingconfigdefinition.md">ForwardingConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PeeringConfig

_Required_: No

_Type_: List of <a href="peeringconfigdefinition.md">PeeringConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateVisibilityConfig

_Required_: No

_Type_: List of <a href="privatevisibilityconfigdefinition.md">PrivateVisibilityConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDirectoryConfig

_Required_: No

_Type_: List of <a href="servicedirectoryconfigdefinition.md">ServiceDirectoryConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### NameServers

Returns the <code>NameServers</code> value.

