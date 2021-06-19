# TF::Turbot::LdapDirectory

The `Turbot LDAP Directory` resource adds support for ldap directories. It is used to create, manage and delete directory settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::LdapDirectory",
    "Properties" : {
        "<a href="#base" title="Base">Base</a>" : <i>String</i>,
        "<a href="#connectivitytestfilter" title="ConnectivityTestFilter">ConnectivityTestFilter</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disabledgroupfilter" title="DisabledGroupFilter">DisabledGroupFilter</a>" : <i>String</i>,
        "<a href="#disableduserfilter" title="DisabledUserFilter">DisabledUserFilter</a>" : <i>String</i>,
        "<a href="#distinguishedname" title="DistinguishedName">DistinguishedName</a>" : <i>String</i>,
        "<a href="#groupmemberofattribute" title="GroupMemberOfAttribute">GroupMemberOfAttribute</a>" : <i>String</i>,
        "<a href="#groupmembershipattribute" title="GroupMembershipAttribute">GroupMembershipAttribute</a>" : <i>String</i>,
        "<a href="#groupobjectfilter" title="GroupObjectFilter">GroupObjectFilter</a>" : <i>String</i>,
        "<a href="#groupprofileidtemplate" title="GroupProfileIdTemplate">GroupProfileIdTemplate</a>" : <i>String</i>,
        "<a href="#groupsearchfilter" title="GroupSearchFilter">GroupSearchFilter</a>" : <i>String</i>,
        "<a href="#groupsyncfilter" title="GroupSyncFilter">GroupSyncFilter</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#profileidtemplate" title="ProfileIdTemplate">ProfileIdTemplate</a>" : <i>String</i>,
        "<a href="#rejectunauthorized" title="RejectUnauthorized">RejectUnauthorized</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#tlsenabled" title="TlsEnabled">TlsEnabled</a>" : <i>Boolean</i>,
        "<a href="#tlsservercertificate" title="TlsServerCertificate">TlsServerCertificate</a>" : <i>String</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#usercanonicalnameattribute" title="UserCanonicalNameAttribute">UserCanonicalNameAttribute</a>" : <i>String</i>,
        "<a href="#userdisplaynameattribute" title="UserDisplayNameAttribute">UserDisplayNameAttribute</a>" : <i>String</i>,
        "<a href="#useremailattribute" title="UserEmailAttribute">UserEmailAttribute</a>" : <i>String</i>,
        "<a href="#userfamilynameattribute" title="UserFamilyNameAttribute">UserFamilyNameAttribute</a>" : <i>String</i>,
        "<a href="#usergivennameattribute" title="UserGivenNameAttribute">UserGivenNameAttribute</a>" : <i>String</i>,
        "<a href="#usermatchfilter" title="UserMatchFilter">UserMatchFilter</a>" : <i>String</i>,
        "<a href="#userobjectfilter" title="UserObjectFilter">UserObjectFilter</a>" : <i>String</i>,
        "<a href="#usersearchattributes" title="UserSearchAttributes">UserSearchAttributes</a>" : <i>[ String, ... ]</i>,
        "<a href="#usersearchfilter" title="UserSearchFilter">UserSearchFilter</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::LdapDirectory
Properties:
    <a href="#base" title="Base">Base</a>: <i>String</i>
    <a href="#connectivitytestfilter" title="ConnectivityTestFilter">ConnectivityTestFilter</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disabledgroupfilter" title="DisabledGroupFilter">DisabledGroupFilter</a>: <i>String</i>
    <a href="#disableduserfilter" title="DisabledUserFilter">DisabledUserFilter</a>: <i>String</i>
    <a href="#distinguishedname" title="DistinguishedName">DistinguishedName</a>: <i>String</i>
    <a href="#groupmemberofattribute" title="GroupMemberOfAttribute">GroupMemberOfAttribute</a>: <i>String</i>
    <a href="#groupmembershipattribute" title="GroupMembershipAttribute">GroupMembershipAttribute</a>: <i>String</i>
    <a href="#groupobjectfilter" title="GroupObjectFilter">GroupObjectFilter</a>: <i>String</i>
    <a href="#groupprofileidtemplate" title="GroupProfileIdTemplate">GroupProfileIdTemplate</a>: <i>String</i>
    <a href="#groupsearchfilter" title="GroupSearchFilter">GroupSearchFilter</a>: <i>String</i>
    <a href="#groupsyncfilter" title="GroupSyncFilter">GroupSyncFilter</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#profileidtemplate" title="ProfileIdTemplate">ProfileIdTemplate</a>: <i>String</i>
    <a href="#rejectunauthorized" title="RejectUnauthorized">RejectUnauthorized</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#tlsenabled" title="TlsEnabled">TlsEnabled</a>: <i>Boolean</i>
    <a href="#tlsservercertificate" title="TlsServerCertificate">TlsServerCertificate</a>: <i>String</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#usercanonicalnameattribute" title="UserCanonicalNameAttribute">UserCanonicalNameAttribute</a>: <i>String</i>
    <a href="#userdisplaynameattribute" title="UserDisplayNameAttribute">UserDisplayNameAttribute</a>: <i>String</i>
    <a href="#useremailattribute" title="UserEmailAttribute">UserEmailAttribute</a>: <i>String</i>
    <a href="#userfamilynameattribute" title="UserFamilyNameAttribute">UserFamilyNameAttribute</a>: <i>String</i>
    <a href="#usergivennameattribute" title="UserGivenNameAttribute">UserGivenNameAttribute</a>: <i>String</i>
    <a href="#usermatchfilter" title="UserMatchFilter">UserMatchFilter</a>: <i>String</i>
    <a href="#userobjectfilter" title="UserObjectFilter">UserObjectFilter</a>: <i>String</i>
    <a href="#usersearchattributes" title="UserSearchAttributes">UserSearchAttributes</a>: <i>
      - String</i>
    <a href="#usersearchfilter" title="UserSearchFilter">UserSearchFilter</a>: <i>String</i>
</pre>

## Properties

#### Base

The BaseDN of all the requests that are sent to LDAP server. In order for your users and groups to be found in an application, they must be located underneath the base DN.
- `distinguished_name` - (Required) This is the username that Turbot will use to authenticate with the directory server after connection has been established. Mostly referred to BindDN in LDAP.
- `tls_enabled` - (Required) TLS setting for the directory server makes sure which certificates should be accepted, rejects those are not signed by a trusted CA.(Boolean)
- `reject_unauthorized` - (Required) When TLS connection is set up, if this is set to `true`, turbot will not verify the TLS certificate that it receives from the server.(Boolean)
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `disabled_user_filter` - (Optional) The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectivityTestFilter

A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Brief description of the purpose and details of the directory.
- `disabled_user_filter` - (Optional) The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisabledGroupFilter

A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisabledUserFilter

The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DistinguishedName

This is the username that Turbot will use to authenticate with the directory server after connection has been established. Mostly referred to BindDN in LDAP.
- `tls_enabled` - (Required) TLS setting for the directory server makes sure which certificates should be accepted, rejects those are not signed by a trusted CA.(Boolean)
- `reject_unauthorized` - (Required) When TLS connection is set up, if this is set to `true`, turbot will not verify the TLS certificate that it receives from the server.(Boolean)
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `disabled_user_filter` - (Optional) The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMemberOfAttribute

The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMembershipAttribute

The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupObjectFilter

The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupProfileIdTemplate

A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupSearchFilter

The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupSyncFilter

Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

ID or `aka` of the parent resource.
- `profile_id_template` - (Required) A template to generate profile id for users authenticated through a ldap directory. For example, email id of the user.
- `password` - (Required) The password of the user specified in directory server.
- `title` - (Required) Short and descriptive name to help identify the directory server.
- `url` - (Required) The FQDN (fully qualified domain name) where the directory server is available. The FQDN also includes the protocol to be used for accessing the server.
- `base` - (Required) The BaseDN of all the requests that are sent to LDAP server. In order for your users and groups to be found in an application, they must be located underneath the base DN.
- `distinguished_name` - (Required) This is the username that Turbot will use to authenticate with the directory server after connection has been established. Mostly referred to BindDN in LDAP.
- `tls_enabled` - (Required) TLS setting for the directory server makes sure which certificates should be accepted, rejects those are not signed by a trusted CA.(Boolean)
- `reject_unauthorized` - (Required) When TLS connection is set up, if this is set to `true`, turbot will not verify the TLS certificate that it receives from the server.(Boolean)
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `disabled_user_filter` - (Optional) The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password of the user specified in directory server.
- `title` - (Required) Short and descriptive name to help identify the directory server.
- `url` - (Required) The FQDN (fully qualified domain name) where the directory server is available. The FQDN also includes the protocol to be used for accessing the server.
- `base` - (Required) The BaseDN of all the requests that are sent to LDAP server. In order for your users and groups to be found in an application, they must be located underneath the base DN.
- `distinguished_name` - (Required) This is the username that Turbot will use to authenticate with the directory server after connection has been established. Mostly referred to BindDN in LDAP.
- `tls_enabled` - (Required) TLS setting for the directory server makes sure which certificates should be accepted, rejects those are not signed by a trusted CA.(Boolean)
- `reject_unauthorized` - (Required) When TLS connection is set up, if this is set to `true`, turbot will not verify the TLS certificate that it receives from the server.(Boolean)
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `disabled_user_filter` - (Optional) The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileIdTemplate

A template to generate profile id for users authenticated through a ldap directory. For example, email id of the user.
- `password` - (Required) The password of the user specified in directory server.
- `title` - (Required) Short and descriptive name to help identify the directory server.
- `url` - (Required) The FQDN (fully qualified domain name) where the directory server is available. The FQDN also includes the protocol to be used for accessing the server.
- `base` - (Required) The BaseDN of all the requests that are sent to LDAP server. In order for your users and groups to be found in an application, they must be located underneath the base DN.
- `distinguished_name` - (Required) This is the username that Turbot will use to authenticate with the directory server after connection has been established. Mostly referred to BindDN in LDAP.
- `tls_enabled` - (Required) TLS setting for the directory server makes sure which certificates should be accepted, rejects those are not signed by a trusted CA.(Boolean)
- `reject_unauthorized` - (Required) When TLS connection is set up, if this is set to `true`, turbot will not verify the TLS certificate that it receives from the server.(Boolean)
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `disabled_user_filter` - (Optional) The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectUnauthorized

When TLS connection is set up, if this is set to `true`, turbot will not verify the TLS certificate that it receives from the server.(Boolean)
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `disabled_user_filter` - (Optional) The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Short and descriptive name to help identify the directory server.
- `url` - (Required) The FQDN (fully qualified domain name) where the directory server is available. The FQDN also includes the protocol to be used for accessing the server.
- `base` - (Required) The BaseDN of all the requests that are sent to LDAP server. In order for your users and groups to be found in an application, they must be located underneath the base DN.
- `distinguished_name` - (Required) This is the username that Turbot will use to authenticate with the directory server after connection has been established. Mostly referred to BindDN in LDAP.
- `tls_enabled` - (Required) TLS setting for the directory server makes sure which certificates should be accepted, rejects those are not signed by a trusted CA.(Boolean)
- `reject_unauthorized` - (Required) When TLS connection is set up, if this is set to `true`, turbot will not verify the TLS certificate that it receives from the server.(Boolean)
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `disabled_user_filter` - (Optional) The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsEnabled

TLS setting for the directory server makes sure which certificates should be accepted, rejects those are not signed by a trusted CA.(Boolean)
- `reject_unauthorized` - (Required) When TLS connection is set up, if this is set to `true`, turbot will not verify the TLS certificate that it receives from the server.(Boolean)
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `disabled_user_filter` - (Optional) The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsServerCertificate

A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

The FQDN (fully qualified domain name) where the directory server is available. The FQDN also includes the protocol to be used for accessing the server.
- `base` - (Required) The BaseDN of all the requests that are sent to LDAP server. In order for your users and groups to be found in an application, they must be located underneath the base DN.
- `distinguished_name` - (Required) This is the username that Turbot will use to authenticate with the directory server after connection has been established. Mostly referred to BindDN in LDAP.
- `tls_enabled` - (Required) TLS setting for the directory server makes sure which certificates should be accepted, rejects those are not signed by a trusted CA.(Boolean)
- `reject_unauthorized` - (Required) When TLS connection is set up, if this is set to `true`, turbot will not verify the TLS certificate that it receives from the server.(Boolean)
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `disabled_user_filter` - (Optional) The disabled user filter of the LDAP directory to connect to.
- `group_object_filter` - (Optional) The filter string that lists all relevant groups in the LDAP server.
- `group_profile_id_template` - (Optional) A template to generate the URN of the profile for groups retrieved from this directory.
**Note**: The profile MUST be unique across all group profiles in Turbot. However, it is possible to have multiple directories map its group to the same Group-Profile.
- `group_search_filter` - (Optional) The provided filter is Nunjucks rendered with `groupname` provided as a data parameter.
- `group_sync_filter` - (Optional) Used to filter out groups of a user which Turbot should sync. If not specified, Turbot will create GroupProfiles for all groups of a user.
**Note**: The host must be resolvable reachable from the network where Turbot is installed.
- `user_object_filter` - (Optional) The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserCanonicalNameAttribute

The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserDisplayNameAttribute

The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserEmailAttribute

The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserFamilyNameAttribute

The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserGivenNameAttribute

The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserMatchFilter

This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserObjectFilter

The filter string that lists all users in the LDAP server.
- `user_match_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a specific user from the directory.
- `user_search_filter` - (Optional) This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserSearchAttributes

This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserSearchFilter

This is overlaid on the `user_object_filter` to query for a sublist of all users in the directory.
- `user_search_attributes` - (Optional) This is a list of properties that will be requested from the LDAP server when requesting for a LDAP user object.
- `user_canonical_name_attribute` - (Optional) The attribute in the LDAP user object which contains the Canonical Name of the user.
- `user_email_attribute` - (Optional) The attribute in the LDAP user object which contains the user's email address.
- `user_display_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's name which will be displayed in Turbot.
- `user_given_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Given Name.
- `user_family_name_attribute` - (Optional) The attribute in the LDAP user object which contains the user's Family Name.
- `tls_server_certificate` - (Optional) A valid and signed certificate from a trusted CA.
- `group_member_of_attribute` - (Optional) The name of the attribute which the LDAP server uses to record group memberships of an object. This is essentially the inverse of `group_membership_attribute`.
- `group_membership_attribute` - (Optional) The name of the attribute which the LDAP server uses to record membership against a group object.
- `connectivity_test_filter` - (Optional) A filter string which will be used to test communication status with the LDAP server.
- `disabled_group_filter` - (Optional) A filter string that when queried in the context of `group_object_filter` returns disabled groups.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for the directory.

_Required_: No

_Type_: String

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

Unique identifier of the ldap directory.

#### ParentAkas

A list of all `akas` for this directory's parent resource.
- `status` - Status of the ldap directory, which defaults to `NEW`. Valid options are `ACTIVE`, `INACTIVE` and `NEW`.
- `id` - Unique identifier of the ldap directory.

#### Status

Status of the ldap directory, which defaults to `NEW`. Valid options are `ACTIVE`, `INACTIVE` and `NEW`.
- `id` - Unique identifier of the ldap directory.

