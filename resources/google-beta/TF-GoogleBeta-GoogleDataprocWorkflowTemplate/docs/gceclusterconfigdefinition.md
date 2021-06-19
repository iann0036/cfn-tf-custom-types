# TF::GoogleBeta::GoogleDataprocWorkflowTemplate GceClusterConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#internaliponly" title="InternalIpOnly">InternalIpOnly</a>" : <i>Boolean</i>,
    "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadatadefinition.md">MetadataDefinition</a>, ... ]</i>,
    "<a href="#network" title="Network">Network</a>" : <i>String</i>,
    "<a href="#privateipv6googleaccess" title="PrivateIpv6GoogleAccess">PrivateIpv6GoogleAccess</a>" : <i>String</i>,
    "<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>" : <i>String</i>,
    "<a href="#serviceaccountscopes" title="ServiceAccountScopes">ServiceAccountScopes</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnetwork" title="Subnetwork">Subnetwork</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
    "<a href="#nodegroupaffinity" title="NodeGroupAffinity">NodeGroupAffinity</a>" : <i>[ <a href="nodegroupaffinitydefinition.md">NodeGroupAffinityDefinition</a>, ... ]</i>,
    "<a href="#reservationaffinity" title="ReservationAffinity">ReservationAffinity</a>" : <i>[ <a href="reservationaffinitydefinition.md">ReservationAffinityDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#internaliponly" title="InternalIpOnly">InternalIpOnly</a>: <i>Boolean</i>
<a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadatadefinition.md">MetadataDefinition</a></i>
<a href="#network" title="Network">Network</a>: <i>String</i>
<a href="#privateipv6googleaccess" title="PrivateIpv6GoogleAccess">PrivateIpv6GoogleAccess</a>: <i>String</i>
<a href="#serviceaccount" title="ServiceAccount">ServiceAccount</a>: <i>String</i>
<a href="#serviceaccountscopes" title="ServiceAccountScopes">ServiceAccountScopes</a>: <i>
      - String</i>
<a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#zone" title="Zone">Zone</a>: <i>String</i>
<a href="#nodegroupaffinity" title="NodeGroupAffinity">NodeGroupAffinity</a>: <i>
      - <a href="nodegroupaffinitydefinition.md">NodeGroupAffinityDefinition</a></i>
<a href="#reservationaffinity" title="ReservationAffinity">ReservationAffinity</a>: <i>
      - <a href="reservationaffinitydefinition.md">ReservationAffinityDefinition</a></i>
</pre>

## Properties

#### InternalIpOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadatadefinition.md">MetadataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIpv6GoogleAccess

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccount

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceAccountScopes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeGroupAffinity

_Required_: No

_Type_: List of <a href="nodegroupaffinitydefinition.md">NodeGroupAffinityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReservationAffinity

_Required_: No

_Type_: List of <a href="reservationaffinitydefinition.md">ReservationAffinityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

