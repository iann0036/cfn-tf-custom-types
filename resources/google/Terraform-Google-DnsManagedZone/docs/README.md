# Terraform::Google::DnsManagedZone

A zone is a subtree of the DNS namespace under one administrative
responsibility. A ManagedZone is a resource that represents a DNS zone
hosted by the Cloud DNS service.


To get more information about ManagedZone, see:

* [API documentation](https://cloud.google.com/dns/api/v1/managedZones)
* How-to Guides
    * [Managing Zones](https://cloud.google.com/dns/zones/)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=dns_managed_zone_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::DnsManagedZone",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dnsname" title="DnsName">DnsName</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#dnssecconfig" title="DnssecConfig">DnssecConfig</a>" : <i>[ <a href="dnssecconfig.md">DnssecConfig</a>, ... ]</i>,
        "<a href="#privatevisibilityconfig" title="PrivateVisibilityConfig">PrivateVisibilityConfig</a>" : <i>[ <a href="privatevisibilityconfig.md">PrivateVisibilityConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#defaultkeyspecs" title="DefaultKeySpecs">DefaultKeySpecs</a>" : <i>[ <a href="defaultkeyspecs.md">DefaultKeySpecs</a>, ... ]</i>,
        "<a href="#networks" title="Networks">Networks</a>" : <i>[ <a href="networks.md">Networks</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::DnsManagedZone
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dnsname" title="DnsName">DnsName</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#dnssecconfig" title="DnssecConfig">DnssecConfig</a>: <i>
      - <a href="dnssecconfig.md">DnssecConfig</a></i>
    <a href="#privatevisibilityconfig" title="PrivateVisibilityConfig">PrivateVisibilityConfig</a>: <i>
      - <a href="privatevisibilityconfig.md">PrivateVisibilityConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#defaultkeyspecs" title="DefaultKeySpecs">DefaultKeySpecs</a>: <i>
      - <a href="defaultkeyspecs.md">DefaultKeySpecs</a></i>
    <a href="#networks" title="Networks">Networks</a>: <i>
      - <a href="networks.md">Networks</a></i>
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

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnssecConfig

_Required_: No

_Type_: List of <a href="dnssecconfig.md">DnssecConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateVisibilityConfig

_Required_: No

_Type_: List of <a href="privatevisibilityconfig.md">PrivateVisibilityConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultKeySpecs

_Required_: No

_Type_: List of <a href="defaultkeyspecs.md">DefaultKeySpecs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

_Required_: No

_Type_: List of <a href="networks.md">Networks</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### NameServers

Returns the <code>NameServers</code> value.

